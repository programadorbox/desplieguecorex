/* =========================================
   1. SISTEMA DE TRADUCCIÓN (Inglés/Español)
   ========================================= */
const langToggle = document.getElementById('lang-toggle');
let currentLang = 'es'; 

const translations = {
  "btn-login": { es: "Ingresar", en: "Login" },
  "mob-nav-contacto": { es: "Contacto", en: "Contact" },
  "mob-btn-login": { es: "Ingresar", en: "Login" },
  "hero-title": { es: "Software a medida para tu operación", en: "Custom software for your operations" },
  "hero-lead": { 
    es: "Soluciones robustas para Minería, Logística, Retail y Gestión Comercial. Centraliza tus operaciones con software diseñado a la medida.", 
    en: "Robust solutions for Mining, Logistics, Retail, and Sales Management. Centralize your operations with custom-designed software." 
  },
  "form-title": { es: "Hablemos", en: "Let's Talk" },
  "form-subtitle": { es: "Déjanos tus datos y te contactaremos.", en: "Leave your details and we will contact you." },
  "lbl-nombre": { es: "Nombre*", en: "Name*" },
  "lbl-email": { es: "Email*", en: "Email*" },
  "lbl-telefono": { es: "Teléfono", en: "Phone" },
  "lbl-interes": { es: "Interés", en: "Interest" },
  "lbl-mensaje": { es: "Mensaje", en: "Message" },
  "opt-operaciones": { es: "Operaciones / Trazabilidad", en: "Operations / Traceability" },
  "opt-mineria": { es: "Minería / Geodata", en: "Mining / Geodata" },
  "opt-flota": { es: "Flota / Transporte", en: "Fleet / Transport" },
  "opt-infraestructura": { es: "Infraestructura", en: "Infrastructure" },
  "opt-talento": { es: "Gestión de Talento", en: "Talent Management" },
  "opt-farma": { es: "Salud / Farma", en: "Health / Pharma" },
  "opt-inmobiliaria": { es: "Inmobiliaria / Ventas", en: "Real Estate / Sales" },
  "opt-otro": { es: "Otro", en: "Other" },
  "about-title": { es: "Sobre CorexAndes", en: "About CorexAndes" },
  "about-desc": { 
    es: "Transformamos operaciones complejas en sistemas simples. Desarrollamos tecnología estratégica para empresas que buscan control total y eficiencia.", 
    en: "We transform complex operations into simple systems. We develop strategic technology for companies seeking total control and efficiency." 
  },
  "li-tech-1": { es: "✔ Arquitectura Segura y Escalable", en: "✔ Secure & Scalable Architecture" },
  "li-tech-2": { es: "✔ Conexión Total entre Sistemas", en: "✔ Total System Integration" },
  "li-tech-3": { es: "✔ Control Operativo Absoluto", en: "✔ Absolute Operational Control" }
};

const dynamicText = {
  placeholder: { es: "Cuéntanos brevemente tu proyecto...", en: "Tell us briefly about your project..." },
  sentBtn: { es: "¡Enviado! Te contactaremos pronto.", en: "Sent! We will contact you soon." }
};

if (langToggle) {
  langToggle.addEventListener('click', () => {
    currentLang = currentLang === 'es' ? 'en' : 'es';
    for (const [id, texts] of Object.entries(translations)) {
      const element = document.getElementById(id);
      if (element) element.innerText = texts[currentLang];
    }
    const translatableElements = document.querySelectorAll('[data-translate]');
    translatableElements.forEach(el => {
      const key = el.getAttribute('data-translate');
      if (translations[key]) el.innerText = translations[key][currentLang];
    });
    const textArea = document.getElementById('txt-mensaje-placeholder');
    if (textArea) textArea.placeholder = dynamicText.placeholder[currentLang];

    langToggle.innerHTML = currentLang === 'es' 
      ? '<span class="active-lang" style="color:#00DFF3">ES</span> / <span class="inactive-lang">EN</span>'
      : '<span class="inactive-lang">ES</span> / <span class="active-lang" style="color:#00DFF3">EN</span>';
    const langToggleMobile = document.getElementById('lang-toggle-mobile');
    if (langToggleMobile) langToggleMobile.innerHTML = langToggle.innerHTML;
  });
}

const langToggleMobile = document.getElementById('lang-toggle-mobile');
if (langToggleMobile) langToggleMobile.addEventListener('click', () => { if(langToggle) langToggle.click(); });

/* =========================================
   2. CARRUSEL INFINITO
   ========================================= */
const slider = document.getElementById('slider');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let scrollSpeed = 0.5, isPaused = false;

function autoScroll() {
  if (window.innerWidth < 992) return;
  if (!isPaused && slider) {
    slider.scrollLeft += scrollSpeed;
    if (slider.scrollLeft >= (slider.scrollWidth / 2)) slider.scrollLeft = 0;
  }
  requestAnimationFrame(autoScroll);
}
if (slider) {
  requestAnimationFrame(autoScroll);
  function manualMove(dir) {
    isPaused = true;
    slider.scrollBy({ left: dir * 300, behavior: 'smooth' });
    setTimeout(() => { isPaused = false; }, 3000);
  }
  if(nextBtn) nextBtn.addEventListener('click', () => manualMove(1));
  if(prevBtn) prevBtn.addEventListener('click', () => manualMove(-1));
}

/* =========================================
   3, 4, 5. INTERACCIÓN, MENÚ, PROGRESO
   ========================================= */
const nameInput = document.querySelector('input[name="nombre"]');
const interestSelect = document.querySelector('select[name="interes"]');
document.querySelectorAll('.card-cta').forEach(link => {
  link.addEventListener('click', () => {
    if (interestSelect) interestSelect.value = link.getAttribute('data-interest');
    if (nameInput) setTimeout(() => { nameInput.focus(); nameInput.classList.add('highlight-focus'); }, 100);
  });
});

const mobileBtn = document.getElementById('mobile-menu-btn');
const mobileDropdown = document.getElementById('mobile-dropdown');
if (mobileBtn && mobileDropdown) mobileBtn.addEventListener('click', () => mobileDropdown.classList.toggle('active'));

window.addEventListener('scroll', () => {
  const scrolled = (document.documentElement.scrollTop / (document.documentElement.scrollHeight - document.documentElement.clientHeight)) * 100;
  const bar = document.getElementById("myBar");
  if (bar) bar.style.width = scrolled + "%";
});

/* /* =========================================
   6. INTEGRACIÓN ENVÍO DJANGO
   ========================================= */
const mainForm = document.getElementById('mainForm');
const submitBtn = document.querySelector('input[type="submit"]');

if (mainForm && submitBtn) {
  mainForm.addEventListener('submit', () => {
    // Aplicamos la clase de éxito
    submitBtn.classList.add('btn-success');
    submitBtn.value = dynamicText.sentBtn[currentLang];
    submitBtn.disabled = true;
  });
}

window.addEventListener('DOMContentLoaded', () => {
    const successMsg = document.querySelector('.mensaje-exito'); 
    if (successMsg && submitBtn) {
        // Aplicamos la clase de éxito al cargar
        submitBtn.classList.add('btn-success');
        submitBtn.value = dynamicText.sentBtn[currentLang];
        submitBtn.disabled = true;
    }
});

/* =========================================
   7. MODAL LOGIN
   ========================================= */
const modal = document.getElementById('custom-modal');
document.querySelectorAll('#btn-login, #mob-btn-login').forEach(btn => btn.addEventListener('click', (e) => {
  e.preventDefault();
  modal.style.display = "flex";
  setTimeout(() => modal.classList.add('active'), 10);
}));

document.getElementById('close-modal-btn').addEventListener('click', () => {
  modal.classList.remove('active');
  setTimeout(() => modal.style.display = "none", 300);
});