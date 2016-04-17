var btn_id = "#pickfiles";//按钮id


UE.registerUI('button',function(editor,uploaderBtn){
    editor.registerCommand(uploaderBtn,{
        execCommand:function(){
            console.log($("#pickfiles"));
            $("#pickfiles").trigger("click");
        }
    });

    var btn = new UE.ui.Button({
        name:uploaderBtn,
        title:"上传图片到又拍云",
        cssRules :'background-position: -500px 0;',
        //点击时执行的命令
        onclick:function () {
            //这里可以不用执行命令,做你自己的操作也可
           editor.execCommand(uploaderBtn);
        }
    });

    return btn;
});


// //并列绑定，File值触发，触发请求
// $(btn_id).change(function(){
//     console.log($(btn_id).val());
//     // UE.getEditor('editor').setContent('ssss');//可以访问到
// });