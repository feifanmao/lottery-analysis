const API = {
    async get(url) {
        const resp = await fetch(url);
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        return resp.json();
    },

    dlt: {
        draws: (limit = 50, offset = 0) => API.get(`/api/dlt/draws?limit=${limit}&offset=${offset}`),
        latest: () => API.get('/api/dlt/latest'),
    },

    ssq: {
        draws: (limit = 50, offset = 0) => API.get(`/api/ssq/draws?limit=${limit}&offset=${offset}`),
        latest: () => API.get('/api/ssq/latest'),
    },

    analysis: {
        frequency: (lottery) => API.get(`/api/analysis/frequency?lottery=${lottery}`),
        missing: (lottery) => API.get(`/api/analysis/missing?lottery=${lottery}`),
        segment: (lottery) => API.get(`/api/analysis/segment?lottery=${lottery}`),
        parity: (lottery) => API.get(`/api/analysis/parity?lottery=${lottery}`),
        sum: (lottery) => API.get(`/api/analysis/sum?lottery=${lottery}`),
        consecutive: (lottery) => API.get(`/api/analysis/consecutive?lottery=${lottery}`),
        repeat: (lottery) => API.get(`/api/analysis/repeat?lottery=${lottery}`),
        ac: (lottery) => API.get(`/api/analysis/ac?lottery=${lottery}`),
        span: (lottery) => API.get(`/api/analysis/span?lottery=${lottery}`),
    },
};
