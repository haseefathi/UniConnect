function load_table() {
    console.log("initializing the datatable");

    console.log("adding text input");
    // Setup - add a text input to each footer cell
    $('#example tfoot th').each(function() {
        var title = $(this).text();
        console.log(title);
        $(this).html('<input type="text" placeholder="Search ' + title + '" />');
    });

    // DataTable
    var table = $('#example').DataTable({
        initComplete: function() {
            // Apply the search
            this.api().columns().every(function() {
                var that = this;

                $('input', this.footer()).on('keyup change clear', function() {
                    if (that.search() !== this.value) {
                        that
                            .search(this.value)
                            .draw();
                    }
                });
            });
        }
    });
}