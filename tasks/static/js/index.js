document.addEventListener('DOMContentLoaded', function () {
    const textarea = document.getElementById('id_description');

    textarea.addEventListener('keyup', function () {
        this.style.overflow = 'hidden';
        this.style.height = 'auto';  
        this.style.height = this.scrollHeight + 'px';
    });

    textarea.style.height = textarea.scrollHeight + 'px';
});