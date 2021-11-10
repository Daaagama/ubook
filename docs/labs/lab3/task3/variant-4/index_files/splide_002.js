const splide = () => {
    new Splide('.splide', {
        type: 'loop',
        width: 470,
        arrows: false,
        autoplay: true,
        breakpoints: {
            480: {
                width: 350
            }
        }
    }).mount();
}

const directionsSlider = () => {
    new Splide('.directions_slider', {
        perPage: 3,
        perMove: 1,
        pagination: false,
        type: 'loop',
        gap: '80px',
        breakpoints: {
            1600: {
                gap: '65px'
            },
            992: {
                perPage: 1,
                padding: {
                    right: '5rem',
                    left: '5rem',
                },
                gap: 25,
            },
            480: {
                perPage: 1,
                padding: {
                    right: 0,
                    left: 0,
                },
            }
        }
    }).mount();
}

const mentorsSplide = () => {
    new Splide('.mentors_splide', {
        type: 'loop',
        perMove: 1,
        perPage: 4,
        rewind: true,
        gap: 60,
        pagination: false,
        breakpoints: {
            1600: {
                perPage: 3,
            },
            1360: {
                perPage: 3,
                gap: 30,
            },
            992: {
                perPage: 1,
                padding: {
                    right: '10rem',
                    left: '10rem',
                },
                pagination: true,
                arrows: false
            },
            480: {
                perPage: 1,
            }
        }
    }).mount();
}

const project = () => {
    new Splide('.project_slider', {
        type: 'loop',
    }).mount();
}

const reviewsVideos = () => {
    new Splide('.reviews_videos', {
        type: 'loop',
        arrows: false,
        padding: {
            right: '5rem',
            left: '5rem',
        },
        breakpoints: {
            480: {
                // width: 343,
                perPage: 1,
                padding: {
                    right: 0,
                    left: 0,
                },
                gap: 5,
            }
        }
    }).mount();
}

const formSplide = () => {
    new Splide('.form_splide', {
        perMove: 1,
        type: 'loop',
        perPage: 2,
        pagination: false,
        gap: 20,
        breakpoints: {
            480: {
                perPage: 1,
                // gap: 120,
                // padding: {
                //     right: 2,
                //     left: 2,
                // },
            }
        }
    }).mount();
}

const formSplideOnline = () => {
    new Splide('.form_splide__online', {
        perMove: 1,
        type: 'loop',
        perPage: 2,
        pagination: false,
        gap: 20,
        breakpoints: {
            480: {
                perPage: 1,
                padding: {
                    right: 0,
                    left: 0,
                },
            }
        }
    }).mount();
}

const salariesSplide = (classBlock) => {
    new Splide('.salaries_splide', {
        type: 'loop',
        padding: {
            right: '3rem',
            left: '3rem',
        },
        arrows: false,
        gap: 10,
    }).mount();
}

const gallerySplide = () => {
    new Splide( '.gallery_splide', {
        type   : 'loop',
        perPage: 4,
        perMove: 1,
        gap: 30,
        pagination: false,
        breakpoints: {
            992: {
                padding: {
                    right: '5rem',
                    left : '5rem',
                },
                perPage: 2,
                gap: 10,
            },

            480: {
                perPage: 2,
                arrows: false,
                padding: {
                    right: '5rem',
                    left : '5rem',
                },
            },
        }
    } ).mount();
}

const directionSplide = () => {
    new Splide( '.direction_splide', {
        type   : 'loop',
        perPage: 2,
        gap: 15,
        padding: {
            right: '5rem',
            left : '5rem',
        },

        breakpoints: {
            480: {
                perPage: 1,
                arrows: false,
                padding: {
                    right: '0',
                    left : '0',
                },
            },
        }
    } ).mount();
}

const freeResultSplide = () => {
    new Splide( '.free_result__splide', {
        type   : 'loop',
        arrows: false,
        padding: {
            right: '5rem',
            left : '5rem',
        },
        breakpoints: {
            480: {
                padding: {
                    right: '0',
                    left : '0',
                },
            },
        }
    } ).mount();
}


const reviewsThanks = () => {
    new Splide( '.reviews_thanks__splide', {
        perPage: 3,
        perMove: 1,
        rewind : true,
        pagination: false,
        gap: 50,
        type: 'loop',
        breakpoints: {
            1200: {
                gap: 25,
            },

            992: {
                pagination: true,
                arrows: false,
                perPage: 1,
                padding: {
                    right: '5rem',
                    left : '5rem',
                },
            },

            480: {
                padding: {
                    right: '0',
                    left : '0',
                },
            },
        }
    } ).mount();
}

