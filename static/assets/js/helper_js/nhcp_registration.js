$('#wizard2').steps({
    headerTag: 'h3',
    bodyTag: 'section',
    autoFocus: true,
    titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
    onStepChanging: function(event, currentIndex, newIndex) {
        if (currentIndex < newIndex) {
            // Step 1 form validation
            if (currentIndex === 0) {
                var fname = $('#firstname').parsley();
                // var fname = $('#datepicker-date').parsley();
                var lname = $('#lastname').parsley();
                console.log('fname.isValid():',fname.isValid())
                console.log('fname.validate():',fname.validate())
                console.log('lname.validate():',lname.validate())
                // validate() function will validate the input fields
                // 
                if (fname.validate() && lname.validate()) {
                    console.log('in if AT LINE 25');
                    // if returned True then wizard is shifted to next step 
                    // return true;
                } 
            }
            // Step 2 form validation
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