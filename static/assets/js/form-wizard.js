(function($) {
    "use strict";

    $('#wizard1').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>'
    });
    $('#wizard2').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
        onStepChanging: function(event, currentIndex, newIndex) {
            // console.log('current index before step 1', currentIndex)
            if (currentIndex < newIndex) {
                // Step 1 form validation
                if (currentIndex === 0) {
                    var fname = $('#firstname').parsley();
                    // var fname = $('#datepicker-date').parsley();
                    var lname = $('#lastname').parsley();
                    // var lname = $('#user_gender').parsley();
                    // if condition is executed when input fields are non-empty
                    // if (fname.isValid() && lname.isValid()) {
                    if (fname.validate() && lname.validate()) {
                        console.log('in if AT LINE 25');
                        return true;
                    } else {
                        // else is executed when input fields are empty
                        // fname and lname is validated and error message is shown
                        fname.validate();
                        lname.validate();
                        console.log('in else AT LINE 31');

                        return false;
                    }
                    // console.log('fname.isValid():',fname.isValid())
                    // console.log('fname.validate():',fname.validate())
                    // console.log('lname.validate():',lname.validate())
                    // if (fname.validate() && lname.validate()) {
                    //     console.log('in if AT LINE 25');
                    //     return true;
                    // } 
                }
                // Step 2 form validation
                console.log('current index after step 1', currentIndex)
                if (currentIndex === 1) {
                    var email = $('#email').parsley();
                    if (email.isValid()) {
                        return true;
                    } else {
                        email.validate();
                    }
                }
                // Always allow step back to the previous step even if the current step is not valid.
            } else {
                return true;
            }
        }
    });
    $('#wizard3').steps({
        headerTag: 'h3',
        bodyTag: 'section',
        autoFocus: true,
        titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
        stepsOrientation: 1
    });

    $('.dropify-clear').click(function() {
        $('.dropify-render img').remove();
        $(".dropify-preview").css("display", "none");
        $(".dropify-clear").css("display", "none");
    });

    //_________accordion-wizard
    var options = {
        mode: 'wizard',
        autoButtonsNextClass: 'btn btn-primary float-end',
        autoButtonsPrevClass: 'btn btn-light',
        stepNumberClass: 'badge rounded-pill bg-primary me-1',
        onSubmit: function() {
            alert('Form submitted!');
            return true;
        }
    }

})(jQuery);

//Function to show image before upload

function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
        reader.onload = function(e) {
            $('.dropify-render img').remove();
            var img = $('<img id="dropify-img">'); //Equivalent: $(document.createElement('img'))
            img.attr('src', e.target.result);
            img.appendTo('.dropify-render');
            $(".dropify-preview").css("display", "block");
            $(".dropify-clear").css("display", "block");
        };
        reader.readAsDataURL(input.files[0]);
    }
}