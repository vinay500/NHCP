document.addEventListener("DOMContentLoaded", function() {
    // Find all table rows in the tbody of the table
    const rows = document.querySelectorAll("#responsive-datatable tbody tr");

    rows.forEach(row => {
        row.addEventListener("click", function() {
            // Assuming 'data-id' is an attribute containing the dependent's ID
            const dependentId = this.getAttribute('mem_id');
            console.log('dependentId: ',dependentId)
            if(dependentId) {
                window.location.href = `/view_dependent/${dependentId}`;
            }
        });
    });
});