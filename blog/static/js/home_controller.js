/* Used for displayed posted date */
const month_names = new Array("January", "February", "March", 
"April", "May", "June", "July", "August", "September", 
"October", "November", "December");


/**
 * Load the articles and page numbering when the home page is entered 
 */
$(document).ready(function(){
    get("loadArticles", {page: "1", category: $("button[name='currentCategory']").text(), 
                            search: $("input[name='search']").val().trim()});
    get("loadCategories", {});
});

/**
 * Load the appropriate articles when a page number is clicked
 */
$(document).on('click', 'button[name ="page"]', function(event){

    const pageID = event.target.id;
    const pageValue = $(this).text()
    var page;

    /* The ids are used to differentiate the starting ".." button with the ending one */
    if ( pageValue==".." ) {
        if (pageID==0)
            page = "1";
        else 
            page = "last";
    }
    else{
        page = pageValue;
    }

    get("loadArticles", {page: page, category: $("button[name='currentCategory']").text(),
                            search: $("input[name='search']").val().trim()});
});

/**
 * Redirect to the page of the article
 */
$(document).on('click', 'button[name ="readArticle"]', function(event){
    document.location.href = "articleDetails?id="+event.target.id
});

/**
 * Load only the appropriate articles when a category is clicked
 */
$(document).on('click', 'span[name ="category"]', function(event){
    $("button[name='currentCategory']").empty();
    $("button[name='currentCategory']").append($(this).text());
    get("loadArticles", {page: "1", category: $(this).text(),
                            search: $("input[name='search']").val().trim()});
});

/**
 * Search when pressed enter
 */
$(document).on('keypress', function(event) {
    var keycode = event.keyCode || event.which;
    if(keycode == '13') {
        //console.log($("input[name='search']").val().trim());
        get("loadArticles", {page: "1", category: $("button[name='currentCategory']").text(), 
                                search: $("input[name='search']").val().trim()}); 
    }
});


/* Get method, factoring code */
function get(url, data){
    if ( url == "loadArticles" ){
        $.get(url, data, function(data, status){
            renderArticles(data);
            renderPageNumbering(data);
        });
    }
    else if ( url == "loadCategories" ){
        $.get(url, data, function(data, status){
            renderCategories(data);
        });
    }
}

/**
 * Loading the articles
 * 
 * @param {*} data received from the server. Contains the articles data
 */
function renderArticles(data){    

    var articles = data['articles']
    $("div[name='articles']").empty();

    // Specific rendering when no article is found for this search
    if ( articles.length == 0 ){
        $("div[name='articles']").append(`
                    <h1 class="mx-auto align-self-center">
                        No article found...
                    </h1>
            `);
    }

    else{

        for (var i=0; i<articles.length; i++){

            /* Specific date format */
            var date  = new Date(articles[i]['date_posted']);
            var day   = date.getDate();
            var month = date.getMonth();
            var year  = date.getFullYear();

            if ( i >= (articles.length-2) ){
                cardWidth = "last-card-width"
            }
            else {
                cardWidth = "card-width"
            }

            $("div[name='articles']").append(`
                <div class="col card mx-3 `+cardWidth+`">
                    <div class="card-body">
                        <h4 class="card-title card-title-article">`+articles[i]['title']+`</h4>
                        <div class="card-subtitle mb-3 text-muted text-left font-italic date-size">By `+articles[i]['author']+` from `+month_names[month]+` `+day+`, `+year+`</div>
                        <p class="card-text text-left card-text-article">`+articles[i]['content']+`</p>
                        <div class="bottom-right">
                            <button class="btn btn-dark active" id=`+articles[i]['id']+` name="readArticle">Read More</button>
                        </div>  
                    </div>
                </div>
            `);
        }
    }
}

/**
 * Loading the page numbering.
 * 
 * @param {*} data received from the server. Contains the page numbers to render and the current page to display.
 */
function renderPageNumbering(data){

    var pages       = data['pages']
    var currentPage = data['currentPage']

    $("div[name='pages']").empty();

    for (var i=0; i<pages.length; i++){

        // Diffentiate the current page and the others. The current page cannot be clicked
        if ( pages[i] == currentPage ){
            var render = "btn btn-secondary";
            var name = ""
        }
        else{
            var render = 'btn btn-outline-dark';
            var name = " name='page' "
        }

        $("div[name='pages']").append(`
            <button class="`+render+`"`+name+` id="`+i+`">`
                +pages[i]+
            `</button>
        `)
    }
}

/**
 * Loading the categories for search.
 * 
 * @param {*} data received from the server. Contains the categories received from the server.
 */
function renderCategories(data){

    var categories = data['categories'];

    for (var i=0; i<categories.length; i++){
        $("#categories").append(`
            <span class="dropdown-item" name="category">`
                +categories[i]["name"]+
            `</span>
        `);
    }
}

