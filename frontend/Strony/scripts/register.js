const form = document.getElementById('reg_form');

form.addEventListener('submit', function(event){
    event.preventDefault();

    const form_data = new FormData(form);

    const firstName = form_data.get('fnameRegister').trim;
    const surrName = form_data.get('snameRegister').trim;
    const gender = form_data.get('genderSelect');
    const password = form_data.get('passOneRegister');
    const confirmPassword = form_data.get('passTwoRegister');
    const email = form_data.get('emailRegister');
    const check = form_data.get('checkBoxAgreeRegister');
    const phone = form_data.get('phoneNum').trim;

    const city = form_data.get('city');
    const street = form_data.get('street');
    const building = form_data.get('buildNum');
    const flatNum = form_data.get('flatNum');


    if ( !check|| !firstName || !surrName || !gender || !password || !confirmPassword || !email || !phone) {
        alert("Enter values in spaces with *");
    }
    else {
        //console.log("Succes!");
        if (password !== confirmPassword) {
            alert("Passwords do not mach");
        }
        if (phone && (!/^\d{9}$/.test(phone))) {
            alert("Numer telefonu musi mieć 9 cyfr");
        }
        alert("Sucess! You can log in now!");
        //WARTOŚCI SIĘ JESZCZE NIE DODAJĄ DO BAZY!!!



        setTimeout(() => {
            window.location.href = "../html/log_in.html";
        }, 300);
    }

})

/*function validateRegistration() {
    const form_data = new FormData(form);

    const firstName = form_data.get('fnameRegister').trim;
    const surrName = form_data.get('snameRegister').trim;
    const gender = form_data.get('genderSelect');
    const password = form_data.get('passOneRegister');
    const confirmPassword = form_data.get('passTwoRegister');
    const email = form_data.get('emailRegister');*/
  /*  const firstName = document.getElementById('fname_r').value.trim();
    const lastName = document.getElementById('sname_r').value.trim();
    const gender = document.getElementById('gender_r').value;
    const password = document.getElementById('pass_one_r').value.trim();
    const confirmPassword = document.getElementById('pass').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const address = document.getElementById('address').value.trim();
    const registerButton = document.getElementById('register-button'); // Użycie id zamiast klasy

    // Resetowanie stylów przycisku
    registerButton.style.backgroundColor = "";
    registerButton.style.color = "";

    // Sprawdzenie wymaganych pól
    if (!firstName || !lastName || !gender || !password || !confirmPassword || !email || !address) {
        registerButton.style.backgroundColor = "#f8d7da"; // Czerwone tło
        registerButton.style.color = "#721c24"; // Czerwony tekst
        alert("Uzupełnij dane z gwiazdką *");
        return;
    }

    // Sprawdzenie zgodności haseł
    if (password !== confirmPassword) {
        registerButton.style.backgroundColor = "#f8d7da"; // Czerwone tło
        registerButton.style.color = "#721c24"; // Czerwony tekst
        alert("Błędne hasła");
        return;
    }

    // Sprawdzenie numeru telefonu (jeśli podany)
    if (phone && (!/^\d{9}$/.test(phone))) {
        registerButton.style.backgroundColor = "#f8d7da"; // Czerwone tło
        registerButton.style.color = "#721c24"; // Czerwony tekst
        alert("Numer telefonu musi mieć 9 cyfr");
        return;
    }

    // Jeśli dane są poprawne
    registerButton.style.backgroundColor = "#d4edda"; // Zielone tło
    registerButton.style.color = "#155724"; // Zielony tekst

    // Przekierowanie na stronę główną po 300 ms
    setTimeout(() => {
        window.location.href = "Strona_Glowna.html";
    }, 300);*/