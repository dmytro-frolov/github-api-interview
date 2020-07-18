import config from 'react-global-configuration'



config.set({
    BackendHost: process.env.REACT_APP_BACKEND_HOST || "http://localhost:8000",
    AuthURL: process.env.REACT_APP_AUTH_URL || "http://localhost:8000/api/v1/authenticate",
})

