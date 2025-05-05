$(document).ready(function() {
    function truncateString(str, maxLength) {
        return str.length > maxLength ? str.substring(0, maxLength) + '...' : str;
    }

    function getSelectedCheckboxValues(name) {
        return $('input[name="' + name + '"]:checked').map(function() {
            return $(this).val();
        }).get();
    }

    function updateURLParams(params) {
        var urlParams = new URLSearchParams();
        if (params['selected_thematiques'].length > 0) {
            params['selected_thematiques'].forEach(function(value) {
                urlParams.append('selected_thematiques', value);
            });
        }
        if (params['selected_periodicities'].length > 0) {
            params['selected_periodicities'].forEach(function(value) {
                urlParams.append('selected_periodicities', value);
            });
        }
        if (params['search']) {
            urlParams.set('search', params['search']);
        }

        var newUrl = urlParams.toString() ? '/tables/?' + urlParams.toString() : '/tables/';
        if (newUrl !== window.location.pathname + window.location.search) {
            history.pushState(params, '', newUrl); // Utiliser pushState pour ajouter une nouvelle entrée à l'historique
        }
    }

    function loadFilteredSubThemes(selectedThematiques, selectedPeriodicities, searchTerm) {
var url = '/filter_sous_thematiques/';
var params = {};
if (selectedThematiques.length > 0) {
    params['selected_thematiques'] = selectedThematiques;
}
if (selectedPeriodicities.length > 0) {
    params['selected_periodicities'] = selectedPeriodicities;
}
if (searchTerm) {
    params['search'] = encodeURIComponent(searchTerm);
}
var apiUrl = url + '?' + $.param(params, true);

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        var subThemeList = $('#subtheme-list');
        subThemeList.empty();

        // *** NOUVEAU : mettre à jour le nombre d'éléments ***
        const count = data.sous_thematiques.length;
        $('#dataset-count').html(`Rechercher parmi les ${count} jeux de données sur <strong>opendatastream</strong>`);

        data.sous_thematiques.forEach(function(subTheme) {
            var truncatedDescription = truncateString(subTheme.description_sous_thematique, 300);
            var cardHtml = `
                <a href="/sous-thematiques/${subTheme.url_slug}/" style="color:#000;">
                    <div class="col-md-12"> 
                        <div class="card" style="margin-bottom: 20px;">
                            <div class="card-header">
                                ${subTheme.thematique_parente}
                            </div>
                            <div class="card-body">
                                <h5 class="card-title">${subTheme.titre}</h5>
                                <p class="card-text">${truncatedDescription}</p>
                                <p>Périodicité: ${subTheme.periodicite}</p>
                            </div>
                        </div>  
                    </div> 
                </a>`;
            subThemeList.append(cardHtml);
        });
    });
}


    function loadFilteredSubThemesFromUrl() {
        var urlParams = new URLSearchParams(window.location.search);
        var selectedThematiques = urlParams.getAll('selected_thematiques');
        var selectedPeriodicities = urlParams.getAll('selected_periodicities');
        var searchTerm = urlParams.get('search') || '';

        $('input[name="thematique"]').prop('checked', false);
        $('input[name="periodicite"]').prop('checked', false);

        selectedThematiques.forEach(function(theme) {
            $('input[name="thematique"][value="' + theme + '"]').prop('checked', true);
        });
        selectedPeriodicities.forEach(function(periodicity) {
            $('input[name="periodicite"][value="' + periodicity + '"]').prop('checked', true);
        });

        $('#recherche-input').val(searchTerm);
        loadFilteredSubThemes(selectedThematiques, selectedPeriodicities, searchTerm);
    }

    loadFilteredSubThemesFromUrl();

    $('input[name="thematique"], input[name="periodicite"], #recherche-input').on('input change', function() {
        var selectedThematiques = getSelectedCheckboxValues('thematique');
        var selectedPeriodicities = getSelectedCheckboxValues('periodicite');
        var searchTerm = $('#recherche-input').val();

        var params = {
            'selected_thematiques': selectedThematiques,
            'selected_periodicities': selectedPeriodicities,
            'search': searchTerm
        };

        updateURLParams(params);
        loadFilteredSubThemes(selectedThematiques, selectedPeriodicities, searchTerm);
    });


    window.onpopstate = function(event) {
        loadFilteredSubThemesFromUrl();
    };
});
