TheUploader = {};

TheUploader.tools = {};



TheUploader.tools.uploader = new plupload.Uploader({
    runtimes : 'html5,flash,silverlight,html4',

    browse_button : 'pickfiles', // you can pass in id...
    container: document.getElementById('uploadfiles-container'), // ... or DOM Element itself

    url : "/examples/upload",

    filters : {
        max_file_size : '10mb',
        mime_types: [
            {title : "Image files", extensions : "jpg,gif,png"},
            {title : "Zip files", extensions : "zip"}
        ]
    },

    init: {
        PostInit: function() {
            console.log('PostInit');
            $('#'+this.browse_button).click(function() {
                uploader.start();
                return false;
            });
        },

        FilesAdded: function(up, files) {
            console.log('FilesAdded');
            plupload.each(files, function(file) {
                // console.log(9999);
            });
        },

        UploadProgress: function(up, file) {
            console.log('[UploadProgress]');
            // document.getElementById(file.id).getElementsByTagName('b')[0].innerHTML = '<span>' + file.percent + "%</span>";
        },

        Error: function(up, err) {
            console.log('Error');
            // document.getElementById('console').innerHTML += "\nError #" + err.code + ": " + err.message;
        }
    }
});


TheUploader.tools.uploader.init();
