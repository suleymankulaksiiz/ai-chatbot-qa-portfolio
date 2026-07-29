import { defineConfig } from '@playwright/test';

export default defineConfig({

    testDir: './tests',

    reporter: [
        ['html']
    ],

    use: {
        baseURL: 'http://localhost:3000',

        screenshot: 'only-on-failure',

        video: 'retain-on-failure',

        trace: 'retain-on-failure'
    },

});