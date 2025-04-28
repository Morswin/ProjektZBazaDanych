const form = document.getElementById('log_in_form');

form.addEventListener('submit', function(event){
    event.preventDefault();
    const form_data = new FormData(form);

    const email = form_data.get('emailLogin');
    const password = form_data.get('passLogIn');

    if (!email || !password) {
        // Jeśli brak e-maila lub hasła
        alert("Type email and/or password");
    }

    //baza danych goofy owo

});