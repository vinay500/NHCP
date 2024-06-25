const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;

// adding on_submit event listener to the form
document.addEventListener("DOMContentLoaded", function () {
    console.log(' in submit event')
    const form = document.querySelector("#forgot_password_form");
  
    form.addEventListener("submit", async function (event) {
      // preventing form from reloading when submitted
      event.preventDefault();
      // fetching user entered details ie., email,password,confirm password
      const email = document.getElementById("forgot_password_mail").value;
      
      console.log('user details', email)
      error_in_signin_data = false
      document.getElementById('email_required_msg').style.display='none'
      document.getElementById('valid_email_required_msg').style.display='none'
      
      document.getElementById("forgot_password_mail").style.borderColor = '#e3e3e3';
      
      // check if email is empty or not
      if (email.length == 0) {
        // error_fields.push("signin_email")
        // error_message_array.push("Email")
        document.getElementById('email_required_msg').style.display='block'
        document.getElementById("forgot_password_mail").style.borderColor = 'red';
        error_in_signin_data = true;
      } 
      else{
        // Check if the email is in correct format
        if (!email.match(emailRegex)) {
            // error_fields.push("signin_email")
            // error_message_array.push("Valid Email")
            document.getElementById('valid_email_required_msg').style.display='block'
            document.getElementById("forgot_password_mail").style.borderColor = 'red';
            error_in_signin_data = true;
          }
      }
      
      // fetching CSRF token from form
      const csrfToken = form.querySelector("[name='csrfmiddlewaretoken']").value;
  
      const formData = new FormData();
  
      formData.append("email", email);
  
      // console log formData object values to make sure they are same as user entered values
      for (const value of formData.values()) {
        console.log('formData', value);
      }
      
      if(!error_in_signin_data){
        try {
            document.getElementById('global-loader').style.display='block';
            const response = await fetch("", {
              method: "POST",
              headers: {
                "X-CSRFToken": csrfToken,
              },
              body: formData,
            });
            if (response.ok) {
              document.getElementById('global-loader').style.display='none';
              let data = await response.text();
              console.log('Server Response:', data);
      
              if (data === 'forgot_password_success') {
                document.getElementById('success_msg').innerText = 'Reset Password Link Sent, Kindly Check Your Mail';
                document.getElementById('success_container').style.display='block';
              } else if (data == "Something Went Wrong, Try Again"){
                document.getElementById('error_msg').innerText = 'Something Went Wrong, Try Again';
                document.getElementById('error_container').style.display='block';
              } else if (data == "Email not Registered"){
                document.getElementById('error_msg').innerText = "Email not Registered, Try with Regsitered Mail";
                document.getElementById('error_container').style.display='block';
              } else{ 
                // Login failed, display error message
                document.getElementById('error_msg').innerText = 'Something went wrong, try again';
                document.getElementById('error_container').style.display='block';
              }
            }
          } catch (error) {
            console.error("Error:", error);
            // Handle the error
            document.getElementById('error_msg').innerText = 'Something went wrong, try again';
            document.getElementById('error_container').style.display='block';
          }
      }
      
    });
  });


function remove_success_container(){
  document.getElementById("success_container").style.display="none";
}

function remove_error_container(){
  document.getElementById("error_container").style.display="none";
}