const clickHandlerOwuItem = (classItem) => {
    const list_item = document.querySelectorAll(`.${classItem}`);
    list_item.forEach(item => {
        item.onclick = function () {
            this.classList.toggle('is-active');
        }
    })
}

const accordion = (elementClass, numChild) => {
    let contentMobile = document.querySelectorAll(elementClass);
    console.log('www')
    contentMobile.forEach(el => {
        el.onclick = () => {

            el.classList.toggle('is-active');
            if (el.classList.contains('is-active')) {
                el.children[numChild].style.height = el.children[numChild].scrollHeight + 'px';
            } else {
                el.children[numChild].style.height = '';
            }
        };

        if (el.classList.contains('is-active')) {
            el.children[numChild].style.height = el.children[numChild].scrollHeight + 'px';
        }
    })
}


if (document.body.clientWidth < 992) {
    clickHandlerOwuItem('owu_item');
}

const closeWindow = (buttonClose) => {
    const close = document.querySelectorAll(buttonClose);
    close.forEach(el => {
        el.onclick = (e) => {
            if (e.target.offsetParent.classList.contains('is-active')) {
                e.target.offsetParent.classList.remove('is-active');
            }
        };
    })
}

const buttonModal = () => {
    document.querySelector('.body-modal').classList.add('is-active');
}

const buttonModalClose = () => {
    document.querySelector('.body-modal').classList.remove('is-active');
}

const videoWindow = (el, video) => {
    let id = el.children[0].dataset.id;
    let videoReviewWrap = '';
    video.classList.add('is-active');
    videoReviewWrap = `
            <iframe class="iframe-video" width="500" height="360" src="https://youtube.com/embed/${id}"
                                    frameborder="0"
                                    allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                                    allowfullscreen id="Youtube"></iframe>
        `;

    video.innerHTML += videoReviewWrap;

}

const dreamWorkAccordion = (classItem) => {
    let items = document.querySelectorAll(classItem);
    items.forEach(el => {

        el.onclick = () => {
            el.classList.toggle('is-active');
            el.classList.contains('is-active')
                ? el.style.height = el.scrollHeight + 'px'
                : el.style.height = '';
        }
    })
}

const scrollMyPage = () => {
    $(window).scroll(function (e) {
        let images = document.querySelectorAll('.your-day_image');
        if ($(this).scrollTop() > 4300) {
            images.forEach(el => el.classList.add('is-active'));
        }
        else {
            images.forEach(el => el.classList.remove('is-active'));
        }

    });
}