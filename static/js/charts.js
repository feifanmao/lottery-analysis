// ECharts 通用配置
const CHART_COLORS = ['#ff4444', '#2196F3', '#4CAF50', '#FF9800', '#9C27B0', '#00BCD4', '#795548', '#607D8B'];

function initChart(domId) {
    const dom = document.getElementById(domId);
    if (!dom) return null;
    return echarts.init(dom);
}

// 频率柱状图
function renderFrequencyChart(chart, data, title) {
    const sorted = [...data].sort((a, b) => a.number - b.number);
    chart.setOption({
        title: { text: title, left: 'center', textStyle: { fontSize: 14 } },
        tooltip: { trigger: 'axis' },
        xAxis: { type: 'category', data: sorted.map(x => x.number), axisLabel: { fontSize: 11 } },
        yAxis: { type: 'value', name: '出现次数' },
        series: [{
            type: 'bar', data: sorted.map(x => x.count),
            itemStyle: {
                color: function(params) {
                    const idx = params.dataIndex;
                    return idx < sorted.length / 3 ? '#ff4444' : idx < sorted.length * 2 / 3 ? '#FF9800' : '#2196F3';
                }
            },
        }],
        grid: { left: 50, right: 20, bottom: 40, top: 50 },
    });
}

// 遗漏值柱状图
function renderMissingChart(chart, data, title) {
    const sorted = [...data].sort((a, b) => a.number - b.number);
    chart.setOption({
        title: { text: title, left: 'center', textStyle: { fontSize: 14 } },
        tooltip: { trigger: 'axis' },
        legend: { data: ['当前遗漏', '最大遗漏', '平均遗漏'], bottom: 0 },
        xAxis: { type: 'category', data: sorted.map(x => x.number), axisLabel: { fontSize: 11 } },
        yAxis: { type: 'value' },
        series: [
            { name: '当前遗漏', type: 'bar', data: sorted.map(x => x.current_missing), itemStyle: { color: '#ff4444' } },
            { name: '最大遗漏', type: 'line', data: sorted.map(x => x.max_missing), lineStyle: { type: 'dashed' }, itemStyle: { color: '#FF9800' } },
            { name: '平均遗漏', type: 'line', data: sorted.map(x => x.avg_missing), lineStyle: { type: 'dotted' }, itemStyle: { color: '#2196F3' } },
        ],
        grid: { left: 50, right: 20, bottom: 60, top: 50 },
    });
}

// 号段饼图
function renderSegmentPie(chart, data, title) {
    chart.setOption({
        title: { text: title, left: 'center', textStyle: { fontSize: 14 } },
        tooltip: { trigger: 'item', formatter: '{b}: {c} ({d}%)' },
        series: [{
            type: 'pie', radius: ['35%', '65%'],
            data: data.map(x => ({ name: x.segment, value: x.total })),
            label: { formatter: '{b}\n{d}%' },
        }],
    });
}

// 走势图
function renderTrendChart(chart, draws, lottery) {
    const issues = draws.map(d => d.issue).reverse();
    let series = [];
    let legendData = [];

    if (lottery === 'dlt') {
        for (let i = 1; i <= 5; i++) {
            const name = `前区${i}`;
            legendData.push(name);
            series.push({
                name, type: 'line', data: draws.map(d => d[`front_${i}`]).reverse(),
                lineStyle: { width: 1.5 }, symbolSize: 4,
            });
        }
        for (let i = 1; i <= 2; i++) {
            const name = `后区${i}`;
            legendData.push(name);
            series.push({
                name, type: 'line', data: draws.map(d => d[`back_${i}`]).reverse(),
                lineStyle: { width: 1.5, type: 'dashed' }, symbolSize: 4,
            });
        }
    } else {
        for (let i = 1; i <= 6; i++) {
            const name = `红球${i}`;
            legendData.push(name);
            series.push({
                name, type: 'line', data: draws.map(d => d[`red_${i}`]).reverse(),
                lineStyle: { width: 1.5 }, symbolSize: 4,
            });
        }
        series.push({
            name: '蓝球', type: 'line', data: draws.map(d => d.blue).reverse(),
            lineStyle: { width: 2, color: '#1565C0' }, itemStyle: { color: '#1565C0' }, symbolSize: 6,
        });
        legendData.push('蓝球');
    }

    chart.setOption({
        tooltip: { trigger: 'axis' },
        legend: { data: legendData, bottom: 0, type: 'scroll' },
        xAxis: { type: 'category', data: issues, axisLabel: { rotate: 45, fontSize: 10 } },
        yAxis: { type: 'value' },
        series,
        dataZoom: [{ type: 'slider', start: 70, end: 100 }],
        grid: { left: 50, right: 20, bottom: 80, top: 20 },
    });
}

// 奇偶/大小比饼图
function renderRatioPie(chart, data, title) {
    chart.setOption({
        title: { text: title, left: 'center', textStyle: { fontSize: 14 } },
        tooltip: { trigger: 'item', formatter: '{b}: {c}次 ({d}%)' },
        series: [{
            type: 'pie', radius: ['35%', '65%'],
            data: data.map(x => ({ name: x.ratio, value: x.count })),
            label: { formatter: '{b}\n{d}%' },
        }],
    });
}

// 和值分布柱状图
function renderSumDistChart(chart, dist, title) {
    const keys = Object.keys(dist).sort();
    chart.setOption({
        title: { text: title, left: 'center', textStyle: { fontSize: 14 } },
        tooltip: { trigger: 'axis' },
        xAxis: { type: 'category', data: keys },
        yAxis: { type: 'value', name: '次数' },
        series: [{ type: 'bar', data: keys.map(k => dist[k]), itemStyle: { color: '#4CAF50' } }],
        grid: { left: 50, right: 20, bottom: 40, top: 50 },
    });
}

// 跨度/AC值分布柱状图
function renderDistChart(chart, data, title, xLabel) {
    chart.setOption({
        title: { text: title, left: 'center', textStyle: { fontSize: 14 } },
        tooltip: { trigger: 'axis' },
        xAxis: { type: 'category', data: data.map(x => x[xLabel] || x.ac || x.span) },
        yAxis: { type: 'value', name: '次数' },
        series: [{ type: 'bar', data: data.map(x => x.count), itemStyle: { color: '#FF9800' } }],
        grid: { left: 50, right: 20, bottom: 40, top: 50 },
    });
}
