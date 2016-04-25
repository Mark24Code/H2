H.util = {}


H.util.xlog = function(msg){
    console.log('>>>>>> log start >>>>>>');
    console.log(msg);
    console.log('<<<<<< log   end <<<<<<');
}

H.util.get_url_arg = function(name){
    if (name){
        var curr_search = location.search;
        curr_search = curr_search.substring(curr_search.indexOf("?")+1,curr_search.length);
        var paraObj = {};
        var paraArray = curr_search.split('&');

        for(var i=0;i<paraArray.length;i++){
            var one_para_dict = paraArray[i];
            var para_key = one_para_dict.split('=')[0];
            var para_value = one_para_dict.split('=')[1];
            paraObj[para_key] = para_value;
        }

        return paraObj[name]
    }else{
        return ""
    }
}
