#Ergasia 12
#python 2.7.10

function getRecipeJson(food)
{
    var apiKey = "your-api-key-here";
    var RecipeID = 196149;
    var url = "http://api2.bigoven.com/recipe/" + RecipeID + "?api_key="+apiKey;
    $.ajax(
    {
        type: "GET",

        dataType: 'json',
        cache: false,
        url: url,
        success: function (data)
        {
            alert('success');
            //console.log(data);
        }
    }
    );
}


food = raw_inout =("dose fagito")
recipie = getrecipeJson(food)
bira = getbearJson(food)
if (len(recipie) > 0)
    print recipie
else
    print "den brethike sintagi"
if (len(bira) > 0)
    print bira
else
    "den vrethike bira"
