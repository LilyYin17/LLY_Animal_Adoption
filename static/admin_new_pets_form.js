function validateForm() {
    var breed = document.forms["admin_new_pets_form"]["breed"].value;
    if (breed == "" || breed == null) {
        alert("breed must be filled out");
        return false;
    }
    var name = document.forms["admin_new_pets_form"]["name"].value;
    if (name == "" || name == null) {
        alert("name must be filled out");
        return false;
    }
    var age = document.forms["admin_new_pets_form"]["age"].value;
    if (age == "" || age == null) {
        alert("age must be filled out");
        return false;
    }
    var img = document.forms["admin_new_pets_form"]["img"].value;
    if (img == "" || img == null) {
        alert("no file selected");
        return false;
    }
}