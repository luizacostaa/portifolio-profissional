const carousel = document.querySelector('.carousel');
const nextBtn = document.getElementById('next-btn');
const prevBtn = document.getElementById('prev-btn');

let currentIndex = 0;
const totalItems = document.querySelectorAll('.noticia').length;
const itemsPerSlide = 3;

// Função para atualizar a posição do carrossel
function updateCarousel() {
  const offset = currentIndex * (100 / itemsPerSlide);
  carousel.style.transform = `translateX(-${offset}%)`;
}

// Botão "Próximo"
nextBtn.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % Math.ceil(totalItems / itemsPerSlide);
  updateCarousel();
});

// Botão "Anterior"
prevBtn.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + Math.ceil(totalItems / itemsPerSlide)) % Math.ceil(totalItems / itemsPerSlide);
  updateCarousel();
});

// Rotação automática
setInterval(() => {
  currentIndex = (currentIndex + 1) % Math.ceil(totalItems / itemsPerSlide);
  updateCarousel();
}, 5000); // Troca a cada 5 segundos