// TaskFlow — Main JavaScript

document.addEventListener('DOMContentLoaded', () => {
    // Stagger card entrance animations
    const columns = document.querySelectorAll('.column-body');
    columns.forEach(col => {
        const cards = col.querySelectorAll('.task-card');
        cards.forEach((card, i) => {
            card.style.animationDelay = `${i * 0.07}s`;
        });
    });

    // Add ripple effect to action buttons
    document.querySelectorAll('.btn-primary, .btn-danger-solid').forEach(btn => {
        btn.addEventListener('click', function (e) {
            const ripple = document.createElement('span');
            ripple.style.cssText = `
                position: absolute;
                border-radius: 50%;
                background: rgba(255,255,255,0.3);
                transform: scale(0);
                animation: ripple-anim 0.5s ease-out;
                pointer-events: none;
            `;
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = (e.clientX - rect.left - size / 2) + 'px';
            ripple.style.top = (e.clientY - rect.top - size / 2) + 'px';
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            ripple.addEventListener('animationend', () => ripple.remove());
        });
    });

    // Smooth hover tilt on task cards
    document.querySelectorAll('.task-card').forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            const rotateX = ((y - centerY) / centerY) * -3;
            const rotateY = ((x - centerX) / centerX) * 3;
            card.style.transform = `translateY(-2px) perspective(500px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) perspective(500px) rotateX(0) rotateY(0)';
        });
    });
});

// Inject ripple keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes ripple-anim {
        to { transform: scale(4); opacity: 0; }
    }
`;
document.head.appendChild(style);
