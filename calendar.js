document.addEventListener('DOMContentLoaded', () => {
    fetch('calendarData.json')
        .then(response => response.json())
        .then(data => {
            const container = document.getElementById('calendar-container');
            container.innerHTML = ''; // 기존 내용 초기화 (필요 시)
            
            data.forEach(item => {
                let modulesHtml = '';
                
                item.modules.forEach(mod => {
                    // 기존 버튼 로직
                    const pdfBtn = mod.lecture_pdf ? `<a href="${mod.lecture_pdf}" class="btn-slide">강의자료</a>` : '';
                    const fingerBtn = mod.finger_exercise ? `<a href="${mod.finger_exercise}" class="btn-finger">Finger Exercise</a>` : '';
                    const downloadBtn = mod.download_file ? `<a href="${mod.download_file}" class="btn-download" download>Download</a>` : '';
                    const videoBtn = mod.video_url ? `<a href="${mod.video_url}" class="btn-video" target="_blank">강의영상</a>` : '';

                    // [추가 부분] 퀴즈 및 정답지 버튼 로직
                    const quizBtn = mod.quiz_pdf ? `<a href="${mod.quiz_pdf}" class="btn-quiz">문제</a>` : '';
                    const answerBtn = mod.quiz_answer ? `<a href="${mod.quiz_answer}" class="btn-answer">정답지</a>` : '';

                    modulesHtml += `
                        <div class="module-item">
                            <div class="module-info">
                                <span class="module-num">Module ${mod.num}</span>
                                <span class="module-topic">${mod.topic}</span>
                            </div>
                            <div class="module-materials">
                                ${pdfBtn} ${fingerBtn} ${videoBtn} ${downloadBtn} ${quizBtn} ${answerBtn}
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
