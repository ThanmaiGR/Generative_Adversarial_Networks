import torch
import torch.nn as nn
from django.core.cache import cache

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
latent_dim = 100


class Generator(nn.Module):
    def __init__(self, latent_dim):
        super(Generator, self).__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 2048 * 4 * 4),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Unflatten(1, (2048, 4, 4)),

            nn.ConvTranspose2d(2048, 1024, 4, 2, 1),  # 8x8
            nn.BatchNorm2d(1024),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose2d(1024, 512, 4, 2, 1),  # 16x16
            nn.BatchNorm2d(512),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose2d(512, 256, 4, 2, 1),  # 32x32
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),

            nn.ConvTranspose2d(256, 3, 4, 2, 1),  # 64x64
            nn.Tanh()
        )

    def forward(self, x):
        return self.model(x)


def get_generator():
    generator = cache.get('generator_model')
    if not generator:
        generator = Generator(latent_dim).to(device)
        generator.load_state_dict(torch.load('display/generator/wgan-gp_gen.pth'))
        generator.eval()  # Ensure the generator is in evaluation mode
        cache.set('generator_model', generator, None)  # None means cache indefinitely
    return generator


def get_image(batch_size=50):
    generator = get_generator()
    noise = torch.randn(batch_size, latent_dim).to(device)
    fake_images = generator(noise)
    fake_images = fake_images * 0.5 + 0.5
    fake_images = torch.permute(fake_images, (0, 2, 3, 1)).detach().cpu().numpy()
    return fake_images
