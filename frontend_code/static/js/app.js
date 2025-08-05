// Soccer Predictions App JavaScript

class SoccerPredictionsApp {
    constructor() {
        this.currentPage = 1;
        this.perPage = 15;
        this.currentFilter = 'all';
        this.teamFilter = '';
        this.matches = [];
        this.filteredMatches = [];
        
        this.initializeEventListeners();
        this.loadMatches();
    }

    initializeEventListeners() {
        // Search functionality
        const searchBtn = document.getElementById('searchBtn');
        const teamFilter = document.getElementById('teamFilter');
        
        if (searchBtn) {
            searchBtn.addEventListener('click', () => this.handleSearch());
        }
        
        if (teamFilter) {
            teamFilter.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    this.handleSearch();
                }
            });
        }

        // Filter buttons
        const filterButtons = document.querySelectorAll('[data-filter]');
        filterButtons.forEach(button => {
            button.addEventListener('click', (e) => {
                this.handleFilterChange(e.target.dataset.filter);
            });
        });

        // Per page selector
        const perPageSelect = document.getElementById('perPage');
        if (perPageSelect) {
            perPageSelect.addEventListener('change', (e) => {
                this.perPage = parseInt(e.target.value);
                this.currentPage = 1;
                this.loadMatches();
            });
        }
    }

    async loadMatches() {
        this.showLoading(true);
        
        try {
            const params = new URLSearchParams({
                page: this.currentPage,
                per_page: this.perPage,
                team: this.teamFilter
            });

            const response = await fetch(`/api/matches?${params}`);
            const data = await response.json();
            
            this.matches = data.matches;
            this.renderMatches();
            this.renderPagination(data.current_page, data.total_pages, data.total_matches);
            
        } catch (error) {
            console.error('Error loading matches:', error);
            this.showError('Failed to load matches. Please try again.');
        } finally {
            this.showLoading(false);
        }
    }

    handleSearch() {
        const teamFilter = document.getElementById('teamFilter');
        this.teamFilter = teamFilter ? teamFilter.value.trim() : '';
        this.currentPage = 1;
        this.loadMatches();
    }

    handleFilterChange(filter) {
        // Update active button
        document.querySelectorAll('[data-filter]').forEach(btn => {
            btn.classList.remove('active');
        });
        event.target.classList.add('active');
        
        this.currentFilter = filter;
        this.currentPage = 1;
        this.loadMatches();
    }

    renderMatches() {
        const container = document.getElementById('matchesContainer');
        if (!container) return;

        container.innerHTML = '';

        if (this.matches.length === 0) {
            container.innerHTML = `
                <div class="col-12 text-center py-5">
                    <i class="fas fa-search fa-3x text-muted mb-3"></i>
                    <h4 class="text-muted">No matches found</h4>
                    <p class="text-muted">Try adjusting your search criteria or filters.</p>
                </div>
            `;
            return;
        }

        this.matches.forEach((match, index) => {
            const matchCard = this.createMatchCard(match, index + 1);
            container.appendChild(matchCard);
        });
    }

    createMatchCard(match, index) {
        const col = document.createElement('div');
        col.className = 'col-12 col-lg-6 col-xl-4 mb-4';
        
        const predictedOutcomeClass = `prediction-${match.predicted_outcome.toLowerCase()}`;
        const eloDiffClass = match.elo_diff > 0 ? 'text-success' : match.elo_diff < 0 ? 'text-danger' : 'text-secondary';
        
        col.innerHTML = `
            <div class="card match-card h-100">
                <div class="card-header bg-light">
                    <div class="d-flex justify-content-between align-items-center">
                        <small class="text-muted">
                            <i class="fas fa-calendar me-1"></i>
                            ${match.date}
                            ${match.time !== 'TBD' ? `<i class="fas fa-clock ms-2 me-1"></i>${match.time}` : ''}
                        </small>
                        <span class="badge bg-secondary">${index}/${this.matches.length}</span>
                    </div>
                </div>
                
                <div class="card-body">
                    <!-- Teams and Score -->
                    <div class="row align-items-center mb-3">
                        <div class="col-5 text-end">
                            <h5 class="mb-1">${match.home_team}</h5>
                            <small class="text-muted">Elo: ${match.home_elo}</small>
                        </div>
                        <div class="col-2 text-center">
                            <div class="vs-circle">VS</div>
                        </div>
                        <div class="col-5 text-start">
                            <h5 class="mb-1">${match.away_team}</h5>
                            <small class="text-muted">Elo: ${match.away_elo}</small>
                        </div>
                    </div>

                    <!-- Prediction Probabilities -->
                    <div class="row mb-3">
                        <div class="col-4 text-center">
                            <div class="prediction-box home-win">
                                <div class="prediction-label">Home Win</div>
                                <div class="prediction-value">${match.home_win_prob}%</div>
                            </div>
                        </div>
                        <div class="col-4 text-center">
                            <div class="prediction-box draw">
                                <div class="prediction-label">Draw</div>
                                <div class="prediction-value">${match.draw_prob}%</div>
                            </div>
                        </div>
                        <div class="col-4 text-center">
                            <div class="prediction-box away-win">
                                <div class="prediction-label">Away Win</div>
                                <div class="prediction-value">${match.away_win_prob}%</div>
                            </div>
                        </div>
                    </div>

                    <!-- Predicted Outcome -->
                    <div class="text-center">
                        <span class="badge fs-6 prediction-badge ${predictedOutcomeClass}">
                            Predicted: ${match.predicted_outcome}
                        </span>
                    </div>

                    <!-- Elo Difference -->
                    <div class="text-center mt-2">
                        <small class="text-muted">
                            Elo Difference: 
                            <span class="fw-bold ${eloDiffClass}">
                                ${match.elo_diff}
                            </span>
                        </small>
                    </div>
                </div>
            </div>
        `;
        
        return col;
    }

    renderPagination(currentPage, totalPages, totalMatches) {
        const pagination = document.getElementById('pagination');
        if (!pagination) return;

        pagination.innerHTML = '';

        if (totalPages <= 1) return;

        // Previous button
        const prevLi = document.createElement('li');
        prevLi.className = `page-item ${currentPage === 1 ? 'disabled' : ''}`;
        prevLi.innerHTML = `
            <a class="page-link" href="#" data-page="${currentPage - 1}">
                <i class="fas fa-chevron-left"></i>
            </a>
        `;
        pagination.appendChild(prevLi);

        // Page numbers
        const startPage = Math.max(1, currentPage - 2);
        const endPage = Math.min(totalPages, currentPage + 2);

        for (let i = startPage; i <= endPage; i++) {
            const li = document.createElement('li');
            li.className = `page-item ${i === currentPage ? 'active' : ''}`;
            li.innerHTML = `<a class="page-link" href="#" data-page="${i}">${i}</a>`;
            pagination.appendChild(li);
        }

        // Next button
        const nextLi = document.createElement('li');
        nextLi.className = `page-item ${currentPage === totalPages ? 'disabled' : ''}`;
        nextLi.innerHTML = `
            <a class="page-link" href="#" data-page="${currentPage + 1}">
                <i class="fas fa-chevron-right"></i>
            </a>
        `;
        pagination.appendChild(nextLi);

        // Add click event listeners
        pagination.querySelectorAll('.page-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const page = parseInt(e.target.dataset.page);
                if (page && page !== currentPage && page >= 1 && page <= totalPages) {
                    this.currentPage = page;
                    this.loadMatches();
                }
            });
        });
    }

    showLoading(show) {
        const spinner = document.getElementById('loadingSpinner');
        if (spinner) {
            spinner.classList.toggle('d-none', !show);
        }
    }

    showError(message) {
        const container = document.getElementById('matchesContainer');
        if (container) {
            container.innerHTML = `
                <div class="col-12 text-center py-5">
                    <i class="fas fa-exclamation-triangle fa-3x text-danger mb-3"></i>
                    <h4 class="text-danger">Error</h4>
                    <p class="text-muted">${message}</p>
                </div>
            `;
        }
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new SoccerPredictionsApp();
});

// Add some utility functions
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-GB', {
        weekday: 'short',
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

function formatTime(timeString) {
    if (timeString === 'TBD') return 'TBD';
    return timeString;
}

// Add smooth scrolling for better UX
document.addEventListener('DOMContentLoaded', () => {
    // Smooth scroll to top when changing pages
    const scrollToTop = () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    };

    // Add scroll to top functionality
    const addScrollToTop = () => {
        const scrollBtn = document.createElement('button');
        scrollBtn.innerHTML = '<i class="fas fa-arrow-up"></i>';
        scrollBtn.className = 'btn btn-primary position-fixed';
        scrollBtn.style.cssText = 'bottom: 20px; right: 20px; z-index: 1000; border-radius: 50%; width: 50px; height: 50px; display: none;';
        scrollBtn.id = 'scrollToTop';
        
        document.body.appendChild(scrollBtn);

        // Show/hide scroll button
        window.addEventListener('scroll', () => {
            if (window.pageYOffset > 300) {
                scrollBtn.style.display = 'block';
            } else {
                scrollBtn.style.display = 'none';
            }
        });

        // Scroll to top on click
        scrollBtn.addEventListener('click', scrollToTop);
    };

    addScrollToTop();
}); 