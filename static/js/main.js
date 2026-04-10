// LifeVault — main.js

document.addEventListener('DOMContentLoaded', () => {
  const messages = document.querySelectorAll('.message');
  messages.forEach((msg) => {
    setTimeout(() => {
      msg.style.opacity = '0';
      msg.style.transform = 'translateX(16px)';
      msg.style.transition = 'all 0.3s ease';
      setTimeout(() => msg.remove(), 300);
    }, 4000);
  });
});
