$('#generate-otp').click(function() {
    const password = document.getElementById("signin_password").value;
    if(!(password.length == 0)){
        console.log('password is not zero');
        var value = $(this).html().trim();
        if (value == 'proceed') {
            $(this).html('proceed');
            $('#login-otp').css('display', "flex");
            $('#mobile-num').css('display', "none");
        } else {
            $(this).html('proceed');
            $('#login-otp').css('display', "flex");
            $('#mobile-num').css('display', "none");
        }
    }
    
})