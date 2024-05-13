$(function() {	
	$('#example1').DataTable({
		language: {
			searchPlaceholder: 'Search...',
			sSearch: '',
			lengthMenu: '_MENU_',
		}
	});
});

function beyond_borders_terms_and_condition_register_btn(checkbx,button_id) {
	console.log('checkbox ',checkbx,' button_id ',button_id)
    var btn = document.getElementById(button_id);
    if (checkbx.checked == true) {
        btn.disabled = false;
		// btn.children[0].href = "/add_dependents_test";
    } else {
        btn.disabled = true;
    }
}