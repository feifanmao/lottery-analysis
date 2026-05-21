// 全局彩票类型状态
let currentLottery = 'dlt';

// 彩票切换
document.querySelectorAll('.switch-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.switch-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentLottery = btn.dataset.lottery;
        if (typeof onPageLoad === 'function') {
            onPageLoad();
        }
    });
});

// 渲染大乐透号码球
function renderDltBalls(data) {
    if (!data) return '<p>暂无数据</p>';
    const front = [data.front_1, data.front_2, data.front_3, data.front_4, data.front_5];
    const back = [data.back_1, data.back_2];
    return `
        <div class="draw-result">
            <div class="draw-issue">第 ${data.issue} 期</div>
            <div class="draw-date">${data.draw_date || ''}</div>
            <div>
                ${front.map(n => `<span class="ball ball-front">${String(n).padStart(2, '0')}</span>`).join('')}
                <span style="margin: 0 8px; color: #999;">|</span>
                ${back.map(n => `<span class="ball ball-back">${String(n).padStart(2, '0')}</span>`).join('')}
            </div>
        </div>
    `;
}

// 渲染双色球号码球
function renderSsqBalls(data) {
    if (!data) return '<p>暂无数据</p>';
    const red = [data.red_1, data.red_2, data.red_3, data.red_4, data.red_5, data.red_6];
    return `
        <div class="draw-result">
            <div class="draw-issue">第 ${data.issue} 期</div>
            <div class="draw-date">${data.draw_date || ''}</div>
            <div>
                ${red.map(n => `<span class="ball ball-red">${String(n).padStart(2, '0')}</span>`).join('')}
                <span style="margin: 0 8px; color: #999;">|</span>
                <span class="ball ball-blue">${String(data.blue).padStart(2, '0')}</span>
            </div>
        </div>
    `;
}

// 渲染开奖历史列表
function renderDrawList(draws, lottery) {
    if (!draws || !draws.length) return '<p>暂无数据</p>';
    let html = '<table class="stat-table"><thead><tr><th>期号</th><th>开奖日期</th><th>开奖号码</th></tr></thead><tbody>';
    for (const d of draws) {
        let nums;
        if (lottery === 'dlt') {
            const front = [d.front_1, d.front_2, d.front_3, d.front_4, d.front_5].map(n => `<span class="ball ball-front" style="width:30px;height:30px;font-size:13px;">${String(n).padStart(2, '0')}</span>`).join('');
            const back = [d.back_1, d.back_2].map(n => `<span class="ball ball-back" style="width:30px;height:30px;font-size:13px;">${String(n).padStart(2, '0')}</span>`).join('');
            nums = front + '<span style="margin:0 4px;color:#ccc;">|</span>' + back;
        } else {
            const red = [d.red_1, d.red_2, d.red_3, d.red_4, d.red_5, d.red_6].map(n => `<span class="ball ball-red" style="width:30px;height:30px;font-size:13px;">${String(n).padStart(2, '0')}</span>`).join('');
            nums = red + '<span style="margin:0 4px;color:#ccc;">|</span>' + `<span class="ball ball-blue" style="width:30px;height:30px;font-size:13px;">${String(d.blue).padStart(2, '0')}</span>`;
        }
        html += `<tr><td>${d.issue}</td><td>${d.draw_date || ''}</td><td>${nums}</td></tr>`;
    }
    html += '</tbody></table>';
    return html;
}
