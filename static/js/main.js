// static/js/main.js
// SmartCart Interactive Features & Mobile Navbar Script

document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('smartNavToggle');
    const navMenu = document.getElementById('smartNavMenu');

    const HAMBURGER_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
    const CLOSE_SVG = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';

    if (toggleBtn && navMenu) {
        toggleBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            const isActive = navMenu.classList.toggle('active');
            toggleBtn.setAttribute('aria-expanded', isActive);
            toggleBtn.innerHTML = isActive ? CLOSE_SVG : HAMBURGER_SVG;
        });

        // Close menu when clicking outside
        document.addEventListener('click', function (e) {
            if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && !toggleBtn.contains(e.target)) {
                navMenu.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.innerHTML = HAMBURGER_SVG;
            }
        });

        // Close menu on Escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.innerHTML = HAMBURGER_SVG;
                toggleBtn.focus();
            }
        });

        // Close menu when clicking a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.innerHTML = HAMBURGER_SVG;
            });
        });
    }
});
