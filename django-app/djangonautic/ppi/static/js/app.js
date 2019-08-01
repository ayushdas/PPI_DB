$(document).ready(function () {
    var table = $('#maintable').DataTable({
        mark: true,
        dom: 'Bfrtip',
        lengthMenu: [
            [10, 25, 50, 100, -1],
            ['10 rows', '25 rows', '50 rows', '100 rows', 'Show All']
        ],
        buttons: [
            'pageLength',
            {
                extend: 'copyHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'excelHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'csvHtml5',
                exportOptions: {
                    columns: ':visible'
                }
            },
            {
                extend: 'print',
                exportOptions: {
                    columns: ':visible'
                }
            },
            // {
            //     extend: 'pdfHtml5',
            //     download: 'open',
            //     exportOptions: {
            //         columns: ':visible'
            //     }
            // },
            'colvis'
        ],
        columDefs: [{
            targets: -1,
            visible: false
        }]
    });
});
