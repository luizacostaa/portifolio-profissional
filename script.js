// script.js - interações básicas


// exibindo ano no rodapé
document.getElementById('year').textContent = new Date().getFullYear();


// navegação móvel
const navToggle = document.getElementById('navToggle');
const mainNav = document.getElementById('mainNav');
navToggle.addEventListener('click', ()=>{
mainNav.classList.toggle('open');
const opened = mainNav.classList.contains('open');
navToggle.setAttribute('aria-label', opened ? 'Fechar menu' : 'Abrir menu');
});


// rolagem suave (polish)
document.querySelectorAll('.main-nav a, .btn[href^="#"]').forEach(link => {
link.addEventListener('click', function(e){
const href = this.getAttribute('href');
if(!href || !href.startsWith('#')) return;
e.preventDefault();
const target = document.querySelector(href);
if(target) target.scrollIntoView({behavior:'smooth',block:'start'});
// fechar menu móvel quando clicar
if(mainNav.classList.contains('open')) mainNav.classList.remove('open');
});
});


// exemplo simples: simular cards de projetos clicáveis
Array.from(document.querySelectorAll('.card')).forEach(card=>{
card.addEventListener('click', ()=>{
alert('Abrir descrição detalhada do projeto (você pode linkar para uma página ou modal).');
})
});

// Scroll arrastando com o mouse
const timelineWrapper = document.getElementById("timelineWrapper");

let isDown = false;
let startX;
let scrollLeft;

timelineWrapper.addEventListener("mousedown", (e) => {
  isDown = true;
  timelineWrapper.classList.add("active");
  startX = e.pageX - timelineWrapper.offsetLeft;
  scrollLeft = timelineWrapper.scrollLeft;
});
timelineWrapper.addEventListener("mouseleave", () => {
  isDown = false;
});
timelineWrapper.addEventListener("mouseup", () => {
  isDown = false;
});
timelineWrapper.addEventListener("mousemove", (e) => {
  if (!isDown) return;
  e.preventDefault();
  const x = e.pageX - timelineWrapper.offsetLeft;
  const walk = (x - startX) * 2; // força do arraste
  timelineWrapper.scrollLeft = scrollLeft - walk;
});