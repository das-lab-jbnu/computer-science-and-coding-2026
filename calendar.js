document.addEventListener('DOMContentLoaded', () => {
    fetch('calendarData.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('calendar-container');
            
            data.forEach(item => {
                let modulesHtml = '';
                
                item.modules.forEach(mod => {
                    // 강의자료, 실습, 영상 버튼이 데이터가 있을 때만 생성되도록 처리
                    const pdfBtn = mod.lecture_pdf ? `<a href="${mod.lecture_pdf}" class="btn-slide">강의자료</a>` : '';
                    const fingerBtn = mod.finger_exercise ? `<a href="${mod.finger_exercise}" class="btn-finger">Finger Exercise</a>` : '';
                    const videoBtn = mod.video_url ? `<a href="${mod.video_url}" class="btn-video" target="_blank">강의영상</a>` : '';

                    modulesHtml += `
                        <div class="module-item">
                            <div class="module-info">
                                <span class="module-num">Module ${mod.num}</span>
                                <span class="module-topic">${mod.topic}</span>
                            </div>
                            <div class="module-materials">
                                ${pdfBtn} ${fingerBtn} ${videoBtn}
                            </div>
                        </div>`;
                });

                const weekSection = `
                    <div class="week-section">
                        <div class="week-header">
                            <span class="week-title">Week ${item.week}</span>
                            <span class="week-date">${item.date}</span>
                        </div>
                        <div class="module-container">
                            ${modulesHtml}
                        </div>
                    </div>`;
                
                container.innerHTML += weekSection;
            });
        })
        .catch(error => console.error('Error loading the calendar data:', error));
});