function validateForm() {
    var breed = document.forms["add_new_pets"]["breed"].value;
    if (breed == "" || breed == null) {
        alert("breed must be filled out");
        return false;
    }
    var name = document.forms["add_new_pets"]["name"].value;
    if (name == "" || name == null) {
        alert("name must be filled out");
        return false;
    }
    var age = document.forms["add_new_pets"]["age"].value;
    if (age == "" || age == null) {
        alert("age must be filled out");
        return false;
    }
}