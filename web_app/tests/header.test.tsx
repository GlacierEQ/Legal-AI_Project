import React from 'react';
import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { SessionProvider } from 'next-auth/react';
import Header from '../components/header';

describe('Header', () => {
  it('renders Home link', () => {
    render(
      <SessionProvider session={null}>
        <Header />
      </SessionProvider>,
    );
    expect(screen.getByText('Home')).toBeInTheDocument();
  });
});
