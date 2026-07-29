import { test, expect } from '@playwright/test';


test('TC_LOGIN_002 - Empty Password Validation', async ({ page }) => {

    await page.goto('/');

    page.on('dialog', async dialog => {

        expect(dialog.message())
            .toBe('Email and password are required');

        await dialog.accept();

    });

    await page.fill('#email', 'test@test.com');

    await page.click('button');

});


test('TC_LOGIN_003 - Empty Email Validation', async ({ page }) => {

    await page.goto('/');

    page.on('dialog', async dialog => {

        expect(dialog.message())
            .toBe('Email and password are required');

        await dialog.accept();

    });

    await page.fill('#password', '123456');

    await page.click('button');

});