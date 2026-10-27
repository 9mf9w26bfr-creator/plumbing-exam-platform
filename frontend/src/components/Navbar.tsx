'use client';

import React from 'react';
import { useLanguage } from '../context/LanguageContext';
import {
  BookOpen,
  GraduationCap,
  Timer,
  AlertTriangle,
  BarChart3,
  ShieldCheck,
  Globe,
  Wrench,
} from 'lucide-react';

interface NavbarProps {
  activeTab: string;
  setActiveTab: (tab: string) => void;
  wrongCount: number;
}

export const Navbar: React.FC<NavbarProps> = ({
  activeTab,
  setActiveTab,
  wrongCount,
}) => {
  const { language, toggleLanguage, t } = useLanguage();

  const navItems = [
    { id: 'chapters', label: t('tabChapters'), icon: BookOpen },
    { id: 'units', label: t('tabUnits'), icon: GraduationCap },
    { id: 'mock', label: t('tabMock'), icon: Timer },
    {
      id: 'wrong',
      label: t('tabWrong'),
      icon: AlertTriangle,
      badge: wrongCount > 0 ? wrongCount : undefined,
    },
    { id: 'analytics', label: t('tabAnalytics'), icon: BarChart3 },
    { id: 'cms', label: t('tabCMS'), icon: ShieldCheck },
  ];

  return (
    <header className="bg-slate-900 border-b border-slate-800 text-slate-100 sticky top-0 z-50 shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo & Platform Info */}
          <div
            onClick={() => setActiveTab('chapters')}
            className="flex items-center space-x-3 cursor-pointer group"
          >
            <div className="w-10 h-10 rounded-lg bg-cyan-600/20 border border-cyan-500/30 flex items-center justify-center text-cyan-400 group-hover:bg-cyan-600/30 transition-colors">
              <Wrench className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <span className="font-bold tracking-tight text-white text-base sm:text-lg">
                  {t('platformTitle')}
                </span>
                <span className="text-xs font-mono uppercase bg-cyan-950 text-cyan-300 px-2 py-0.5 rounded border border-cyan-800">
                  C&G Level 2/3
                </span>
              </div>
              <p className="text-xs text-slate-400 hidden sm:block">
                {t('platformSub')}
              </p>
            </div>
          </div>

          {/* Bilingual Language Switcher Button */}
          <div className="flex items-center space-x-3">
            <button
              onClick={toggleLanguage}
              className="flex items-center space-x-2 px-3 py-1.5 rounded-md bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 text-xs font-medium transition shadow-sm"
              title="Toggle English / 中文"
            >
              <Globe className="w-4 h-4 text-cyan-400" />
              <span>{language === 'zh' ? '繁中 / EN' : 'EN / 繁中'}</span>
              <span className="w-2 h-2 rounded-full bg-cyan-400 animate-pulse"></span>
            </button>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="flex space-x-1 sm:space-x-2 overflow-x-auto py-2 border-t border-slate-800/80 text-sm scrollbar-none">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveTab(item.id)}
                className={`flex items-center space-x-2 px-3 py-1.5 rounded-md text-xs sm:text-sm font-medium transition whitespace-nowrap ${
                  isActive
                    ? 'bg-cyan-600 text-white shadow-sm'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span>{item.label}</span>
                {item.badge !== undefined && (
                  <span
                    className={`ml-1 text-xs px-1.5 py-0.2 rounded-full font-bold ${
                      isActive
                        ? 'bg-rose-500 text-white'
                        : 'bg-rose-500/20 text-rose-300 border border-rose-500/30'
                    }`}
                  >
                    {item.badge}
                  </span>
                )}
              </button>
            );
          })}
        </nav>
      </div>
    </header>
  );
};
