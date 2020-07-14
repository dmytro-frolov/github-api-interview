import config from 'react-global-configuration'


config.set({
    BackendHost: process.env.REACT_APP_BACKEND_HOST,
    AuthURL: process.env.REACT_APP_AUTH_URL,
})

