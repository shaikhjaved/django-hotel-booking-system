
function validateControl(control, e) {
    debugger
    let key = control.attr('type') === undefined ? control[0].nodeName.toLowerCase() : control.attr('type');
    switch (key) {
        case 'text':
            if (!control.val().trim().length > 0) {
                control.closest('.column').removeClass('is-valid').addClass('is-invalid');
                control.focus()
                e.preventDefault();
                return false;
            } else {
                control.closest('.column').removeClass('is-invalid').addClass('is-valid');
            }
            break;
        case 'number':
            if (!control.val().trim().length > 0) {
                control.closest('.column').removeClass('is-valid').addClass('is-invalid');
                control.focus()
                e.preventDefault();
                return false;
            } else {
                control.closest('.column').removeClass('is-invalid').addClass('is-valid');
            }
            break;
        case 'textarea':
            if (!control.val().trim().length > 0) {
                control.closest('.column').removeClass('is-valid').addClass('is-invalid');
                control.focus()
                e.preventDefault();
                return false;
            } else {
                control.closest('.column').removeClass('is-invalid').addClass('is-valid');
            }
            break;
        case 'select':
            if (control.find(":selected").val() === "0") {
                control.closest('.column').removeClass('is-valid').addClass('is-invalid');
                control.focus()
                e.preventDefault();
                return false;
            } else {
                control.closest('.column').removeClass('is-invalid').addClass('is-valid');
            }
            break;
        case 'email':
            if (!control.val().trim().length > 0) {
                control.closest('.column').removeClass('is-valid').addClass('is-invalid');
                control.focus()
                e.preventDefault();
                return false;
            } else {
                control.closest('.column').removeClass('is-invalid').addClass('is-valid');
            }
            break;
        default:
            break;
    }
};