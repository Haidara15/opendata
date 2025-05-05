document.addEventListener('DOMContentLoaded', function () {
    const accordionHeaders = document.querySelectorAll('.accordion-header');
    const accordionBodies = document.querySelectorAll('.accordion-body');
    const accordionIcons = document.querySelectorAll('.accordion-header .accordion-icon');

    // OUVRIR TOUS les accordéons par défaut
    accordionBodies.forEach((body, index) => {
        body.classList.add('open');
        body.style.maxHeight = body.scrollHeight + 'px';
        if (accordionIcons[index]) {
            accordionIcons[index].setAttribute('name', 'chevron-up-outline');
        }
    });

    // Comportement au clic : toggle ouvrir/fermer
    accordionHeaders.forEach((header) => {
        const body = header.nextElementSibling;
        const icon = header.querySelector('.accordion-icon');

        header.addEventListener('click', function () {
            const isOpen = body.classList.contains('open');

            if (isOpen) {
                // Fermer si ouvert
                body.classList.remove('open');
                body.style.maxHeight = null;
                icon.setAttribute('name', 'chevron-down-outline');
            } else {
                // Ouvrir si fermé
                body.classList.add('open');
                body.style.maxHeight = body.scrollHeight + 'px';
                icon.setAttribute('name', 'chevron-up-outline');
            }
        });
    });
});
