//button是类型名(系统)，editor是系统传入的实例(系统)，uiName是自定义组件名
UE.registerUI('button',function(editor,uploaderBtn){
    //注册按钮执行时的command命令，使用命令默认就会带有回退操作
    //使用editor名字空间，捆绑一个命令 uploaderBtn --> execCMD:function(){...}
    editor.registerCommand(uploaderBtn,{
        execCommand:function(){
            $('#upyunUploader-Btn').click();
        }
    });

    //创建一个button
    var btn = new UE.ui.Button({
        //按钮的名字
        name:uploaderBtn,
        //提示：鼠标悬停提示
        title:"上传图片到又拍云",
        //需要添加的额外样式，指定icon图标，这里默认使用一个重复的icon
        cssRules :'background-position: -500px 0;',
        //点击时执行的命令
        onclick:function () {
            //这里可以不用执行命令,做你自己的操作也可
            //捆绑上面自己注册的函数
           editor.execCommand(uploaderBtn);
        }
    });

    //因为你是添加button,所以需要返回这个button
    return btn;
}/*index 指定添加到工具栏上的那个位置，默认时追加到最后,editorId 指定这个UI是那个编辑器实例上的，默认是页面上所有的编辑器都会添加这个按钮*/);