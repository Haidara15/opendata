
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

        var newUrl = urlParams.toString() ? '/thematiques/' + thematiqueSlug + '/?' + urlParams.toString() : '/thematiques/' + thematiqueSlug + '/';

        if (newUrl !== window.location.pathname + window.location.search) {
            history.pushState(params, '', newUrl);
        }
    }

    function loadFilteredSubThemes(selectedThematiques, selectedPeriodicities) {
        var url = '/thematiques/' + thematiqueSlug + '/';
        var params = {};
        if (selectedThematiques.length > 0) {
            params['selected_thematiques'] = selectedThematiques;
        }
        if (selectedPeriodicities.length > 0) {
            params['selected_periodicities'] = selectedPeriodicities;
        }

        fetch(url + '?' + $.param(params, true), {
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
        })
        .then(response => response.json())
        .then(data => {
            var subThemeList = $('#sous-thematiques-list');
            subThemeList.empty();

            data.sous_thematiques.forEach(function(subTheme) {
                var truncatedDescription = truncateString(subTheme.description_sous_thematique, 300);
                var cardHtml = `
                    <a href="/sous-thematiques/${subTheme.slug}/" style="color:#000;">
                        <div class="col-md-12"> 
                            <div class="card" style="margin-bottom: 20px;">
                                <div class="card-header">
                                    ${subTheme.titre}
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

        $('input[name="thematique"]').prop('checked', false);
        $('input[name="periodicite"]').prop('checked', false);

        selectedThematiques.forEach(function(theme) {
            $('input[name="thematique"][value="' + theme + '"]').prop('checked', true);
        });
        selectedPeriodicities.forEach(function(periodicity) {
            $('input[name="periodicite"][value="' + periodicity + '"]').prop('checked', true);
        });

        loadFilteredSubThemes(selectedThematiques, selectedPeriodicities);
    }

    loadFilteredSubThemesFromUrl();

    $('#theme-detail-checkboxes input[type="checkbox"], #periodicite-detail-checkboxes input[type="checkbox"]').on('change', function() {
        var selectedThematiques = getSelectedCheckboxValues('thematique');
        var selectedPeriodicities = getSelectedCheckboxValues('periodicite');

        var params = {
            'selected_thematiques': selectedThematiques,
            'selected_periodicities': selectedPeriodicities
        };

        updateURLParams(params);
        loadFilteredSubThemes(selectedThematiques, selectedPeriodicities);
    });

    window.onpopstate = function(event) {
        loadFilteredSubThemesFromUrl();
    };
});
