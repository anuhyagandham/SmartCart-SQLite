// static/js/main.js
// SmartCart Interactive Features & Mobile Navbar Script

document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('smartNavToggle');
    const navMenu = document.getElementById('smartNavMenu');

    if (toggleBtn && navMenu) {
        toggleBtn.addEventListener('click', function (e) {
            e.stopPropagation();
            const isActive = navMenu.classList.toggle('active');
            toggleBtn.setAttribute('aria-expanded', isActive);
            toggleBtn.innerHTML = isActive ? '✕' : '☰';
        });

        // Close menu when clicking outside
        document.addEventListener('click', function (e) {
            if (navMenu.classList.contains('active') && !navMenu.contains(e.target) && e.target !== toggleBtn) {
                navMenu.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.innerHTML = '☰';
            }
        });

        // Close menu on Escape key
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.innerHTML = '☰';
                toggleBtn.focus();
            }
        });

        // Close menu when clicking a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(function (link) {
            link.addEventListener('click', function () {
                navMenu.classList.remove('active');
                toggleBtn.setAttribute('aria-expanded', 'false');
                toggleBtn.innerHTML = '☰';
            });
        });
    }
});
