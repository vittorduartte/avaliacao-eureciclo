$(document).on("change", ".file-input", function () {
    const filename = this.value;
    $('span.file-label').text(filename);
    $('span.file-name').text(filename);
})

$(document).on("click", ".back-to-send", function () {
    document.location.replace("/")
})
