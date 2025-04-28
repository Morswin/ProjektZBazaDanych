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