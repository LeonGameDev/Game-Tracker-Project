console.log('My Game Shelf is ready!');

document.querySelectorAll('.danger').forEach(button => {
    button.addEventListener('click', (event) => {
        if (!confirm('Delete this game?')) {
            event.preventDefault();
        }
    });
});
