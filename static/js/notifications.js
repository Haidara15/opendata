function showNotification(message, type = "success") {
    const notification = document.getElementById('notification');

    const maxLength = 150;
    if (message.length > maxLength) {
        message = message.substring(0, maxLength) + '...';
    }

    notification.innerHTML = `
        <button onclick="closeNotification()" class="close-btn">&times;</button>
        <div>${message}</div>
    `;

    notification.style.backgroundColor = type === "error" ? "#dc3545" : "#ccc";

    notification.classList.add('visible');
    notification.classList.remove('hidden');

    setTimeout(() => {
        notification.classList.remove('visible');
        notification.classList.add('hidden');
    }, 6000);
}

function closeNotification() {
    const notification = document.getElementById('notification');
    notification.classList.remove('visible');
    notification.classList.add('hidden');
}
