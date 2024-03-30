window.alert = function(message) {
    var modal = new bootstrap.Modal(document.getElementById('myModal'));
    document.getElementById('modalMessage').innerText = message;
    modal.show();
}