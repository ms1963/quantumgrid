"""
QuantumGrid ULTIMATE - Optimized v3.5.0
Maximum performance + Perfect UI alignment

Cross-platform: Windows, macOS, Linux
Python 3.7+ required

Installation:
    pip install pygame

Usage:
    python quantumgrid_ultimate.py

Author:  Michael Stal, 2026
Version: 3.5.0 (Optimized & Aligned)
License: MIT
"""

import pygame
import random
import math
import json
import sys
from pathlib import Path
from typing import List, Tuple, Optional, Set, Dict

VERSION = "3.5.0"

pygame.init()

# Constants
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
FPS = 120
GRID_SIZE = 7
CELL_SIZE = 90
GRID_PADDING = 10
CLICK_COOLDOWN = 20  # Further reduced for even faster response

SAVE_FILE = Path("quantumgrid_save.json")

# Colors
class Colors:
    DEEP_SPACE = (10, 10, 30)
    DARK_PURPLE = (25, 20, 45)
    NEON_BLUE = (0, 217, 255)
    NEON_PINK = (255, 107, 157)
    NEON_GREEN = (57, 255, 20)
    NEON_YELLOW = (255, 234, 0)
    NEON_PURPLE = (191, 64, 191)
    GOLD = (255, 215, 0)
    WHITE = (255, 255, 255)
    DARK_CELL = (30, 30, 60)
    RED = (255, 50, 50)
    OVERLAY = (0, 0, 0, 180)

class GameState:
    MENU = 1
    PLAYING = 2
    PAUSED = 3
    GAME_OVER = 4
    TUTORIAL = 5

class TextCache:
    """Pre-render all text to avoid slow font.render() calls"""
    def __init__(self):
        self.cache = {}
        self._init_fonts()
        self._prerender_all()
    
    def _init_fonts(self):
        self.title_font = pygame.font.Font(None, 72)
        self.large_font = pygame.font.Font(None, 48)
        self.medium_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 28)
        self.tiny_font = pygame.font.Font(None, 20)
    
    def _prerender_all(self):
        """Pre-render ALL text that will be used in the game"""
        print("  Pre-rendering text...")
        
        # Numbers 0-9 in different fonts and colors
        for num in range(10):
            self.cache[('large', str(num), Colors.WHITE)] = self.large_font.render(str(num), True, Colors.WHITE)
            self.cache[('medium', str(num), Colors.WHITE)] = self.medium_font.render(str(num), True, Colors.WHITE)
            self.cache[('small', str(num), Colors.WHITE)] = self.small_font.render(str(num), True, Colors.WHITE)
        
        # Common UI text
        ui_texts = [
            ('title', 'QUANTUMGRID', Colors.NEON_BLUE),
            ('title', 'TUTORIAL', Colors.NEON_GREEN),
            ('title', 'PAUSED', Colors.NEON_YELLOW),
            ('title', 'GAME OVER', Colors.NEON_PINK),
            ('small', 'Strategic Puzzle Game', Colors.NEON_GREEN),
            ('medium', 'SCORE', Colors.NEON_YELLOW),
            ('medium', 'NEXT TILES', Colors.NEON_BLUE),
            ('tiny', 'QUANTUM ENERGY', Colors.NEON_PURPLE),
            ('medium', 'NEW HIGH SCORE!', Colors.GOLD),
            ('medium', 'BOARD FULL!', Colors.NEON_PINK),
            ('medium', 'No moves remaining!', Colors.WHITE),
            ('medium', 'PLAY', Colors.WHITE),
            ('medium', 'TUTORIAL', Colors.WHITE),
            ('medium', 'QUIT', Colors.WHITE),
            ('medium', 'RESUME', Colors.WHITE),
            ('medium', 'RESTART', Colors.WHITE),
            ('medium', 'MAIN MENU', Colors.WHITE),
            ('medium', 'PLAY AGAIN', Colors.WHITE),
            ('small', 'NEW GAME', Colors.WHITE),
            ('small', 'PREVIOUS', Colors.WHITE),
            ('small', 'NEXT', Colors.WHITE),
            ('small', 'START PLAYING', Colors.WHITE),
            ('tiny', 'PAUSE', Colors.WHITE),
            ('tiny', 'HELP', Colors.WHITE),
        ]
        
        for font_name, text, color in ui_texts:
            font = getattr(self, f'{font_name}_font')
            self.cache[(font_name, text, color)] = font.render(text, True, color)
        
        # Tutorial content
        tutorial_texts = [
            'How to Play', 'Advanced Features', 'Tips Tricks',
            'Click on any empty cell to place the current tile (shown in gold)',
            'Create patterns of 3 or more tiles in a row, column, or diagonal',
            'Different patterns give different points:',
            '  Sum equals 15: +50 points',
            '  Product is a prime number: +75 points',
            '  Fibonacci sequence (e.g., 1-1-2 or 2-3-5): +100 points',
            '  All powers of 2 (e.g., 1-2-4 or 2-4-8): +125 points',
            'COMBO MULTIPLIER:',
            'Create multiple patterns in one move to multiply your score!',
            'QUANTUM ENERGY:',
            'Press Q to use quantum power and gain +5 extra moves',
            'Earn more quantum energy by leveling up',
            'LEVEL UP:',
            'Every 1000 points = new level + 10 bonus moves + quantum energy',
            "Plan ahead using the 'Next Tiles' preview",
            'Look for Fibonacci sequences: 1-1-2, 1-2-3, 2-3-5, 3-5-8',
            'Powers of 2 are: 1, 2, 4, 8 (highest scoring pattern!)',
            'Save quantum powers for when you\'re running low on moves',
            'Press F to toggle FPS display for performance monitoring',
            '',
        ]
        
        for text in tutorial_texts:
            self.cache[('large', text, Colors.NEON_YELLOW)] = self.large_font.render(text, True, Colors.NEON_YELLOW)
            self.cache[('small', text, Colors.WHITE)] = self.small_font.render(text, True, Colors.WHITE)
        
        # Rules panel
        rules = [
            "3+ in a row: Sum=15 (+50) | Prime Product (+75) | Fibonacci (+100) | Powers of 2 (+125)",
            "Multiple patterns = COMBO MULTIPLIER! | Press Q for Quantum Power (+5 moves)",
            "Level up every 1000 points | Press F to toggle FPS | Press H for help"
        ]
        for rule in rules:
            self.cache[('tiny', rule, Colors.NEON_GREEN)] = self.tiny_font.render(rule, True, Colors.NEON_GREEN)
        
        # Page indicators
        for i in range(1, 4):
            text = f"Page {i} of 3"
            self.cache[('tiny', text, Colors.NEON_BLUE)] = self.tiny_font.render(text, True, Colors.NEON_BLUE)
        
        # Version
        self.cache[('tiny', f'v{VERSION}', Colors.DARK_PURPLE)] = self.tiny_font.render(f'v{VERSION}', True, Colors.DARK_PURPLE)
        
        # Pre-render common level/score/moves text
        for i in range(1, 101):
            self.cache[('small', f'LEVEL {i}', Colors.NEON_PINK)] = self.small_font.render(f'LEVEL {i}', True, Colors.NEON_PINK)
        
        for i in range(0, 201):
            self.cache[('small', f'MOVES: {i}', Colors.NEON_GREEN)] = self.small_font.render(f'MOVES: {i}', True, Colors.NEON_GREEN)
            self.cache[('small', f'MOVES: {i}', Colors.NEON_PINK)] = self.small_font.render(f'MOVES: {i}', True, Colors.NEON_PINK)
        
        print("  Text cache ready!")
    
    def get(self, font_name: str, text: str, color: Tuple[int, int, int]) -> pygame.Surface:
        """Get cached text or render on demand"""
        key = (font_name, text, color)
        if key not in self.cache:
            font = getattr(self, f'{font_name}_font')
            self.cache[key] = font.render(text, True, color)
        return self.cache[key]

class Cell:
    # Static cache for all cell surfaces
    _cell_cache = {}
    
    def __init__(self, row: int, col: int, x: int, y: int, size: int, text_cache: TextCache):
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.size = size
        self.value: Optional[int] = None
        self.hover = False
        self.highlight = False
        self.highlight_time = 0.0
        self.text_cache = text_cache
    
    def reset(self):
        self.value = None
        self.hover = False
        self.highlight = False
        self.highlight_time = 0.0
    
    def update(self, dt: float):
        if self.highlight:
            self.highlight_time += dt
            if self.highlight_time > 1.0:
                self.highlight = False
                self.highlight_time = 0.0
    
    def draw(self, surface: pygame.Surface):
        # Cache key
        cache_key = (self.size, self.value, self.hover, self.highlight)
        
        if cache_key not in Cell._cell_cache:
            # Create cell surface
            cell_surf = pygame.Surface((self.size, self.size))
            cell_surf.fill(Colors.DARK_CELL)
            
            # Border
            border_color = Colors.NEON_BLUE if self.hover else Colors.NEON_PURPLE
            if self.highlight:
                border_color = Colors.GOLD
            pygame.draw.rect(cell_surf, border_color, cell_surf.get_rect(), 2, border_radius=10)
            
            # Value
            if self.value is not None:
                text_surf = self.text_cache.get('large', str(self.value), Colors.WHITE)
                text_rect = text_surf.get_rect(center=(self.size // 2, self.size // 2))
                cell_surf.blit(text_surf, text_rect)
            
            Cell._cell_cache[cache_key] = cell_surf
        
        surface.blit(Cell._cell_cache[cache_key], (self.x, self.y))
    
    def is_empty(self) -> bool:
        return self.value is None

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text: str, 
                 color: Tuple[int, int, int], text_cache: TextCache, font_name: str = 'medium'):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover = False
        self.text_cache = text_cache
        self.font_name = font_name
        self._cached_normal = None
        self._cached_hover = None
        self._create_cache()
    
    def _create_cache(self):
        # Normal state
        self._cached_normal = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(self._cached_normal, self.color, self._cached_normal.get_rect(), border_radius=10)
        pygame.draw.rect(self._cached_normal, Colors.WHITE, self._cached_normal.get_rect(), 2, border_radius=10)
        text_surf = self.text_cache.get(self.font_name, self.text, Colors.WHITE)
        text_rect = text_surf.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self._cached_normal.blit(text_surf, text_rect)
        
        # Hover state
        hover_color = tuple(min(255, int(c * 1.3)) for c in self.color)
        self._cached_hover = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(self._cached_hover, hover_color, self._cached_hover.get_rect(), border_radius=10)
        pygame.draw.rect(self._cached_hover, Colors.WHITE, self._cached_hover.get_rect(), 2, border_radius=10)
        self._cached_hover.blit(text_surf, text_rect)
    
    def update(self, mouse_pos: Tuple[int, int]):
        self.hover = self.rect.collidepoint(mouse_pos)
    
    def draw(self, surface: pygame.Surface):
        surf = self._cached_hover if self.hover else self._cached_normal
        surface.blit(surf, self.rect.topleft)
    
    def is_clicked(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)

class QuantumGridGame:
    def __init__(self):
        print("Initializing QuantumGrid ULTRA-FAST...")
        
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(f"QuantumGrid v{VERSION}")
        
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = GameState.MENU
        self.needs_redraw = True
        
        # Text cache - THIS IS THE KEY!
        self.text_cache = TextCache()
        
        # Game state
        self.score = 0
        self.level = 1
        self.moves_remaining = 25
        self.quantum_energy = 3
        self.high_score = self.load_high_score()
        self.combo_count = 0
        self.last_score_gain = 0
        self.last_score_time = 0.0
        self.game_over_reason = ""
        
        # Grid
        self.cells: List[List[Cell]] = []
        self.next_tiles: List[int] = []
        self.grid_offset_x = 50
        self.grid_offset_y = 150
        
        # UI
        self.buttons: Dict[str, Button] = {}
        self.tutorial_page = 0
        self.max_tutorial_pages = 3
        self.last_click_time = 0
        self.show_fps = False
        self.fps_history = []
        
        # Cached surfaces
        print("  Creating background...")
        self._background_cache = self._create_background()
        self._tutorial_cache = {}
        
        print("  Setting up game...")
        self.setup_buttons()
        self.setup_grid()
        self.generate_next_tiles()
        
        print("Ready!\n")
    
    def _create_background(self) -> pygame.Surface:
        bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        
        for y in range(0, WINDOW_HEIGHT, 20):
            progress = y / WINDOW_HEIGHT
            r = int(Colors.DEEP_SPACE[0] + (Colors.DARK_PURPLE[0] - Colors.DEEP_SPACE[0]) * progress)
            g = int(Colors.DEEP_SPACE[1] + (Colors.DARK_PURPLE[1] - Colors.DEEP_SPACE[1]) * progress)
            b = int(Colors.DEEP_SPACE[2] + (Colors.DARK_PURPLE[2] - Colors.DEEP_SPACE[2]) * progress)
            pygame.draw.line(bg, (r, g, b), (0, y), (WINDOW_WIDTH, y), 20)
        
        for _ in range(30):
            x = random.randint(0, WINDOW_WIDTH)
            y = random.randint(0, WINDOW_HEIGHT)
            size = random.randint(1, 2)
            pygame.draw.circle(bg, Colors.WHITE, (x, y), size)
        
        return bg
    
    def setup_buttons(self):
        menu_y = 300
        self.buttons['play'] = Button(WINDOW_WIDTH//2 - 150, menu_y, 300, 60, 
                                      "PLAY", Colors.NEON_BLUE, self.text_cache)
        self.buttons['tutorial'] = Button(WINDOW_WIDTH//2 - 150, menu_y + 80, 300, 60,
                                          "TUTORIAL", Colors.NEON_GREEN, self.text_cache)
        self.buttons['quit'] = Button(WINDOW_WIDTH//2 - 150, menu_y + 160, 300, 60,
                                      "QUIT", Colors.NEON_PINK, self.text_cache)
        
        panel_x = self.grid_offset_x + GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 40
        panel_y = self.grid_offset_y + 710
        
        self.buttons['new_game'] = Button(panel_x + 10, panel_y, 280, 45,
                                         "NEW GAME", Colors.NEON_BLUE, self.text_cache, 'small')
        self.buttons['pause'] = Button(panel_x + 10, panel_y + 55, 135, 40,
                                       "PAUSE", Colors.NEON_YELLOW, self.text_cache, 'tiny')
        self.buttons['help'] = Button(panel_x + 155, panel_y + 55, 135, 40,
                                      "HELP", Colors.NEON_GREEN, self.text_cache, 'tiny')
        
        pause_y = WINDOW_HEIGHT // 2
        self.buttons['resume'] = Button(WINDOW_WIDTH//2 - 150, pause_y - 60, 300, 60,
                                       "RESUME", Colors.NEON_GREEN, self.text_cache)
        self.buttons['restart'] = Button(WINDOW_WIDTH//2 - 150, pause_y + 20, 300, 60,
                                        "RESTART", Colors.NEON_YELLOW, self.text_cache)
        self.buttons['menu'] = Button(WINDOW_WIDTH//2 - 150, pause_y + 100, 300, 60,
                                      "MAIN MENU", Colors.NEON_PINK, self.text_cache)
        
        self.buttons['play_again'] = Button(WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2 + 50, 300, 60,
                                           "PLAY AGAIN", Colors.NEON_GREEN, self.text_cache)
        self.buttons['menu_go'] = Button(WINDOW_WIDTH//2 - 150, WINDOW_HEIGHT//2 + 130, 300, 60,
                                         "MAIN MENU", Colors.NEON_BLUE, self.text_cache)
        
        self.buttons['tutorial_prev'] = Button(WINDOW_WIDTH//2 - 250, WINDOW_HEIGHT - 100, 200, 50,
                                              "PREVIOUS", Colors.NEON_BLUE, self.text_cache, 'small')
        self.buttons['tutorial_next'] = Button(WINDOW_WIDTH//2 + 50, WINDOW_HEIGHT - 100, 200, 50,
                                              "NEXT", Colors.NEON_BLUE, self.text_cache, 'small')
        self.buttons['tutorial_close'] = Button(WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT - 100, 200, 50,
                                                "START PLAYING", Colors.NEON_GREEN, self.text_cache, 'small')
    
    def setup_grid(self):
        self.cells = []
        for row in range(GRID_SIZE):
            cell_row = []
            for col in range(GRID_SIZE):
                x = self.grid_offset_x + col * (CELL_SIZE + GRID_PADDING)
                y = self.grid_offset_y + row * (CELL_SIZE + GRID_PADDING)
                cell = Cell(row, col, x, y, CELL_SIZE, self.text_cache)
                cell_row.append(cell)
            self.cells.append(cell_row)
    
    def generate_next_tiles(self):
        self.next_tiles = [random.randint(1, 9) for _ in range(3)]
    
    def reset_game(self):
        self.score = 0
        self.level = 1
        self.moves_remaining = 25
        self.quantum_energy = 3
        self.combo_count = 0
        self.last_score_gain = 0
        self.last_score_time = 0.0
        self.game_over_reason = ""
        
        for row in self.cells:
            for cell in row:
                cell.reset()
        
        self.generate_next_tiles()
        self.state = GameState.PLAYING
        self.needs_redraw = True
    
    def load_high_score(self) -> int:
        try:
            if SAVE_FILE.exists():
                with open(SAVE_FILE, 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except:
            pass
        return 0
    
    def save_high_score(self):
        try:
            with open(SAVE_FILE, 'w') as f:
                json.dump({'high_score': self.high_score, 'version': VERSION}, f)
        except:
            pass
    
    def is_board_full(self) -> bool:
        """Check if the board has no empty cells"""
        for row in self.cells:
            for cell in row:
                if cell.is_empty():
                    return False
        return True
    
    def update(self, dt: float):
        dt = min(dt, 0.1)
        
        self.fps_history.append(self.clock.get_fps())
        if len(self.fps_history) > 60:
            self.fps_history.pop(0)
        
        if self.state == GameState.PLAYING:
            for row in self.cells:
                for cell in row:
                    cell.update(dt)
        
        if self.last_score_gain > 0:
            self.last_score_time += dt
            if self.last_score_time > 2.0:
                self.last_score_gain = 0
                self.last_score_time = 0.0
                self.needs_redraw = True
    
    def draw(self):
        if not self.needs_redraw:
            return
        
        self.screen.blit(self._background_cache, (0, 0))
        
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_game()
            self.draw_pause_overlay()
        elif self.state == GameState.GAME_OVER:
            self.draw_game()
            self.draw_game_over()
        elif self.state == GameState.TUTORIAL:
            self.draw_tutorial()
        
        if self.show_fps and self.fps_history:
            avg_fps = sum(self.fps_history) / len(self.fps_history)
            fps_surf = self.text_cache.get('tiny', f"FPS: {avg_fps:.0f}", Colors.NEON_GREEN)
            self.screen.blit(fps_surf, (10, 10))
        
        version_surf = self.text_cache.get('tiny', f'v{VERSION}', Colors.DARK_PURPLE)
        self.screen.blit(version_surf, (WINDOW_WIDTH - 60, WINDOW_HEIGHT - 25))
        
        pygame.display.flip()
        self.needs_redraw = False
    
    def draw_menu(self):
        title_surf = self.text_cache.get('title', 'QUANTUMGRID', Colors.NEON_BLUE)
        title_rect = title_surf.get_rect(center=(WINDOW_WIDTH // 2, 150))
        self.screen.blit(title_surf, title_rect)
        
        subtitle_surf = self.text_cache.get('small', 'Strategic Puzzle Game', Colors.NEON_GREEN)
        subtitle_rect = subtitle_surf.get_rect(center=(WINDOW_WIDTH // 2, 220))
        self.screen.blit(subtitle_surf, subtitle_rect)
        
        if self.high_score > 0:
            hs_surf = self.text_cache.get('medium', f"High Score: {self.high_score:,}", Colors.GOLD)
            hs_rect = hs_surf.get_rect(center=(WINDOW_WIDTH // 2, 260))
            self.screen.blit(hs_surf, hs_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        for button_name in ['play', 'tutorial', 'quit']:
            self.buttons[button_name].update(mouse_pos)
            self.buttons[button_name].draw(self.screen)
    
    def draw_game(self):
        title_surf = self.text_cache.get('title', 'QUANTUMGRID', Colors.NEON_BLUE)
        title_rect = title_surf.get_rect(center=(WINDOW_WIDTH // 2, 50))
        self.screen.blit(title_surf, title_rect)
        
        self.draw_grid()
        self.draw_score_panel()
        self.draw_next_tiles_panel()
        self.draw_rules_panel()
        
        mouse_pos = pygame.mouse.get_pos()
        for button_name in ['new_game', 'pause', 'help']:
            self.buttons[button_name].update(mouse_pos)
            self.buttons[button_name].draw(self.screen)
        
        if self.combo_count > 1 and self.last_score_time < 2.0:
            combo_surf = self.text_cache.get('large', f"{self.combo_count}x COMBO!", Colors.GOLD)
            combo_rect = combo_surf.get_rect(center=(WINDOW_WIDTH // 2, self.grid_offset_y - 50))
            self.screen.blit(combo_surf, combo_rect)
        
        if self.last_score_gain > 0 and self.last_score_time < 2.0:
            score_surf = self.text_cache.get('large', f"+{self.last_score_gain}", Colors.NEON_GREEN)
            score_rect = score_surf.get_rect(center=(
                self.grid_offset_x + (GRID_SIZE * (CELL_SIZE + GRID_PADDING)) // 2,
                self.grid_offset_y + GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 60
            ))
            self.screen.blit(score_surf, score_rect)
    
    def draw_grid(self):
        grid_rect = pygame.Rect(
            self.grid_offset_x - 20,
            self.grid_offset_y - 20,
            GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 20,
            GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 20
        )
        pygame.draw.rect(self.screen, Colors.NEON_BLUE, grid_rect, 2, border_radius=15)
        
        for row in self.cells:
            for cell in row:
                cell.draw(self.screen)
    
    def draw_score_panel(self):
        panel_x = self.grid_offset_x + GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 40
        panel_y = self.grid_offset_y
        panel_width = 300
        
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, 400)
        pygame.draw.rect(self.screen, Colors.DARK_CELL, panel_rect, border_radius=15)
        pygame.draw.rect(self.screen, Colors.NEON_PURPLE, panel_rect, 3, border_radius=15)
        
        y = panel_y + 20
        
        score_label = self.text_cache.get('medium', 'SCORE', Colors.NEON_YELLOW)
        score_rect = score_label.get_rect(center=(panel_x + panel_width // 2, y))
        self.screen.blit(score_label, score_rect)
        y += 50
        
        score_surf = self.text_cache.get('large', f"{self.score:,}", Colors.WHITE)
        score_rect = score_surf.get_rect(center=(panel_x + panel_width // 2, y))
        self.screen.blit(score_surf, score_rect)
        y += 80
        
        if self.high_score > 0:
            hs_surf = self.text_cache.get('tiny', f"Best: {self.high_score:,}", Colors.GOLD)
            hs_rect = hs_surf.get_rect(center=(panel_x + panel_width // 2, y))
            self.screen.blit(hs_surf, hs_rect)
            y += 40
        
        # Level text
        level_text = f"LEVEL {self.level}"
        level_surf = self.text_cache.get('small', level_text, Colors.NEON_PINK)
        level_rect = level_surf.get_rect(center=(panel_x + panel_width // 2, y))
        self.screen.blit(level_surf, level_rect)
        y += 60
        
        # Moves text
        moves_color = Colors.NEON_GREEN if self.moves_remaining > 10 else Colors.NEON_PINK
        moves_text = f"MOVES: {self.moves_remaining}"
        moves_surf = self.text_cache.get('small', moves_text, moves_color)
        moves_rect = moves_surf.get_rect(center=(panel_x + panel_width // 2, y))
        self.screen.blit(moves_surf, moves_rect)
        y += 60
        
        # QUANTUM ENERGY label
        energy_label = self.text_cache.get('tiny', 'QUANTUM ENERGY', Colors.NEON_PURPLE)
        energy_rect = energy_label.get_rect(center=(panel_x + panel_width // 2, y))
        self.screen.blit(energy_label, energy_rect)
        y += 35  # Space between label and orbs
        
        # Draw quantum energy orbs - PROPERLY ALIGNED NOW
        orb_radius = 20
        orb_spacing = 70
        # Calculate starting x to center all 3 orbs
        total_width = 3 * orb_radius * 2 + 2 * (orb_spacing - orb_radius * 2)
        start_x = panel_x + (panel_width - total_width) // 2 + orb_radius
        
        for i in range(3):
            orb_x = start_x + i * orb_spacing
            orb_y = y
            
            if i < self.quantum_energy:
                pygame.draw.circle(self.screen, Colors.NEON_PURPLE, (orb_x, orb_y), orb_radius)
            else:
                pygame.draw.circle(self.screen, Colors.DARK_CELL, (orb_x, orb_y), orb_radius)
            pygame.draw.circle(self.screen, Colors.WHITE, (orb_x, orb_y), orb_radius, 2)
    
    def draw_next_tiles_panel(self):
        panel_x = self.grid_offset_x + GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 40
        panel_y = self.grid_offset_y + 440
        panel_width = 300
        
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, 250)
        pygame.draw.rect(self.screen, Colors.DARK_CELL, panel_rect, border_radius=15)
        pygame.draw.rect(self.screen, Colors.NEON_BLUE, panel_rect, 3, border_radius=15)
        
        title_surf = self.text_cache.get('medium', 'NEXT TILES', Colors.NEON_BLUE)
        title_rect = title_surf.get_rect(center=(panel_x + panel_width // 2, panel_y + 30))
        self.screen.blit(title_surf, title_rect)
        
        for i, tile in enumerate(self.next_tiles[:3]):
            tile_y = panel_y + 80 + i * 55
            tile_rect = pygame.Rect(panel_x + 50, tile_y, 200, 45)
            
            color = Colors.GOLD if i == 0 else Colors.DARK_PURPLE
            pygame.draw.rect(self.screen, color, tile_rect, border_radius=10)
            pygame.draw.rect(self.screen, Colors.NEON_BLUE, tile_rect, 2, border_radius=10)
            
            tile_surf = self.text_cache.get('large', str(tile), Colors.WHITE)
            tile_text_rect = tile_surf.get_rect(center=(panel_x + panel_width // 2, tile_y + 22))
            self.screen.blit(tile_surf, tile_text_rect)
    
    def draw_rules_panel(self):
        panel_x = self.grid_offset_x
        panel_y = self.grid_offset_y + GRID_SIZE * (CELL_SIZE + GRID_PADDING) + 20
        panel_width = GRID_SIZE * (CELL_SIZE + GRID_PADDING) - 20
        
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, 120)
        pygame.draw.rect(self.screen, Colors.DARK_CELL, panel_rect, border_radius=15)
        pygame.draw.rect(self.screen, Colors.NEON_GREEN, panel_rect, 2, border_radius=15)
        
        rules = [
            "3+ in a row: Sum=15 (+50) | Prime Product (+75) | Fibonacci (+100) | Powers of 2 (+125)",
            "Multiple patterns = COMBO MULTIPLIER! | Press Q for Quantum Power (+5 moves)",
            "Level up every 1000 points | Press F to toggle FPS | Press H for help"
        ]
        
        y = panel_y + 20
        for rule in rules:
            rule_surf = self.text_cache.get('tiny', rule, Colors.NEON_GREEN)
            rule_rect = rule_surf.get_rect(center=(panel_x + panel_width // 2, y))
            self.screen.blit(rule_surf, rule_rect)
            y += 35
    
    def draw_pause_overlay(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill(Colors.OVERLAY)
        self.screen.blit(overlay, (0, 0))
        
        paused_surf = self.text_cache.get('title', 'PAUSED', Colors.NEON_YELLOW)
        paused_rect = paused_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 150))
        self.screen.blit(paused_surf, paused_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        for button_name in ['resume', 'restart', 'menu']:
            self.buttons[button_name].update(mouse_pos)
            self.buttons[button_name].draw(self.screen)
    
    def draw_game_over(self):
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill(Colors.OVERLAY)
        self.screen.blit(overlay, (0, 0))
        
        go_surf = self.text_cache.get('title', 'GAME OVER', Colors.NEON_PINK)
        go_rect = go_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 200))
        self.screen.blit(go_surf, go_rect)
        
        # Show reason for game over
        if self.game_over_reason:
            reason_surf = self.text_cache.get('medium', self.game_over_reason, Colors.WHITE)
            reason_rect = reason_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 140))
            self.screen.blit(reason_surf, reason_rect)
        
        score_surf = self.text_cache.get('medium', f"Final Score: {self.score:,}", Colors.WHITE)
        score_rect = score_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 80))
        self.screen.blit(score_surf, score_rect)
        
        level_surf = self.text_cache.get('medium', f"Level Reached: {self.level}", Colors.NEON_GREEN)
        level_rect = level_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 20))
        self.screen.blit(level_surf, level_rect)
        
        if self.score >= self.high_score:
            hs_surf = self.text_cache.get('medium', 'NEW HIGH SCORE!', Colors.GOLD)
            hs_rect = hs_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30))
            self.screen.blit(hs_surf, hs_rect)
        
        mouse_pos = pygame.mouse.get_pos()
        for button_name in ['play_again', 'menu_go']:
            self.buttons[button_name].update(mouse_pos)
            self.buttons[button_name].draw(self.screen)
    
    def draw_tutorial(self):
        if self.tutorial_page not in self._tutorial_cache:
            self._tutorial_cache[self.tutorial_page] = self._create_tutorial_page(self.tutorial_page)
        
        self.screen.blit(self._tutorial_cache[self.tutorial_page], (0, 0))
        
        mouse_pos = pygame.mouse.get_pos()
        
        if self.tutorial_page > 0:
            self.buttons['tutorial_prev'].update(mouse_pos)
            self.buttons['tutorial_prev'].draw(self.screen)
        
        if self.tutorial_page < self.max_tutorial_pages - 1:
            self.buttons['tutorial_next'].update(mouse_pos)
            self.buttons['tutorial_next'].draw(self.screen)
        else:
            self.buttons['tutorial_close'].update(mouse_pos)
            self.buttons['tutorial_close'].draw(self.screen)
    
    def _create_tutorial_page(self, page: int) -> pygame.Surface:
        surf = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        
        title_surf = self.text_cache.get('title', 'TUTORIAL', Colors.NEON_GREEN)
        title_rect = title_surf.get_rect(center=(WINDOW_WIDTH // 2, 80))
        surf.blit(title_surf, title_rect)
        
        if page == 0:
            title = 'How to Play'
            content = [
                "Click on any empty cell to place the current tile (shown in gold)",
                "",
                "Create patterns of 3 or more tiles in a row, column, or diagonal",
                "",
                "Different patterns give different points:",
                "  Sum equals 15: +50 points",
                "  Product is a prime number: +75 points",
                "  Fibonacci sequence (e.g., 1-1-2 or 2-3-5): +100 points",
                "  All powers of 2 (e.g., 1-2-4 or 2-4-8): +125 points",
            ]
        elif page == 1:
            title = 'Advanced Features'
            content = [
                "COMBO MULTIPLIER:",
                "Create multiple patterns in one move to multiply your score!",
                "",
                "QUANTUM ENERGY:",
                "Press Q to use quantum power and gain +5 extra moves",
                "Earn more quantum energy by leveling up",
                "",
                "LEVEL UP:",
                "Every 1000 points = new level + 10 bonus moves + quantum energy",
            ]
        else:
            title = 'Tips & Tricks'
            content = [
                "Plan ahead using the 'Next Tiles' preview",
                "",
                "Look for Fibonacci sequences: 1-1-2, 1-2-3, 2-3-5, 3-5-8",
                "",
                "Powers of 2 are: 1, 2, 4, 8 (highest scoring pattern!)",
                "",
                "Save quantum powers for when you're running low on moves",
                "",
                "Press F to toggle FPS display for performance monitoring",
            ]
        
        title_surf = self.text_cache.get('large', title, Colors.NEON_YELLOW)
        title_rect = title_surf.get_rect(center=(WINDOW_WIDTH // 2, 200))
        surf.blit(title_surf, title_rect)
        
        y = 280
        for line in content:
            line_surf = self.text_cache.get('small', line, Colors.WHITE)
            line_rect = line_surf.get_rect(center=(WINDOW_WIDTH // 2, y))
            surf.blit(line_surf, line_rect)
            y += 40
        
        page_surf = self.text_cache.get('tiny', f"Page {page + 1} of 3", Colors.NEON_BLUE)
        page_rect = page_surf.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150))
        surf.blit(page_surf, page_rect)
        
        return surf
    
    def handle_cell_click(self, row: int, col: int):
        if not (0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE):
            return
        
        cell = self.cells[row][col]
        
        if not cell.is_empty():
            return
        
        if not self.next_tiles:
            return
        
        current = self.next_tiles[0]
        cell.value = current
        
        self.next_tiles.pop(0)
        self.next_tiles.append(random.randint(1, 9))
        
        self.moves_remaining -= 1
        
        self.check_patterns()
        
        # Check for game over conditions
        if self.moves_remaining <= 0:
            self.game_over("No moves remaining!")
        elif self.is_board_full():
            self.game_over("BOARD FULL!")
        
        self.needs_redraw = True
    
    def check_patterns(self):
        patterns_found = 0
        total_points = 0
        matched_cells: Set[Tuple[int, int]] = set()
        
        # Check rows and columns
        for i in range(GRID_SIZE):
            row_values = [self.cells[i][j].value for j in range(GRID_SIZE)]
            points, matches = self.check_line(row_values)
            if points > 0:
                patterns_found += 1
                total_points += points
                matched_cells.update([(i, j) for j in matches])
            
            col_values = [self.cells[j][i].value for j in range(GRID_SIZE)]
            points, matches = self.check_line(col_values)
            if points > 0:
                patterns_found += 1
                total_points += points
                matched_cells.update([(j, i) for j in matches])
        
        # Check diagonals
        diag1 = [self.cells[i][i].value for i in range(GRID_SIZE)]
        diag2 = [self.cells[i][GRID_SIZE-1-i].value for i in range(GRID_SIZE)]
        
        for diag_idx, diag in enumerate([diag1, diag2]):
            points, matches = self.check_line(diag)
            if points > 0:
                patterns_found += 1
                total_points += points
                if diag_idx == 0:
                    matched_cells.update([(i, i) for i in matches])
                else:
                    matched_cells.update([(i, GRID_SIZE-1-i) for i in matches])
        
        self.combo_count = patterns_found
        if patterns_found > 1:
            total_points *= patterns_found
        
        if matched_cells:
            for row, col in matched_cells:
                self.cells[row][col].highlight = True
        
        if total_points > 0:
            self.last_score_gain = total_points
            self.last_score_time = 0.0
            self.score += total_points
            
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            
            new_level = (self.score // 1000) + 1
            if new_level > self.level:
                self.level = new_level
                self.moves_remaining += 10
                self.quantum_energy = min(3, self.quantum_energy + 1)
    
    def check_line(self, line: List[Optional[int]]) -> Tuple[int, List[int]]:
        numbers = [(i, x) for i, x in enumerate(line) if x is not None and 1 <= x <= 9]
        
        if len(numbers) < 3:
            return 0, []
        
        points = 0
        matches = set()
        
        for i in range(len(numbers) - 2):
            seq_indices = [numbers[i][0], numbers[i+1][0], numbers[i+2][0]]
            seq = [numbers[i][1], numbers[i+1][1], numbers[i+2][1]]
            
            # Sum = 15
            if sum(seq) == 15:
                points += 50
                matches.update(seq_indices)
            
            # Prime product
            product = seq[0] * seq[1] * seq[2]
            if self.is_prime(product):
                points += 75
                matches.update(seq_indices)
            
            # Fibonacci
            if seq[0] + seq[1] == seq[2]:
                points += 100
                matches.update(seq_indices)
            
            # Powers of 2
            if all(self.is_power_of_2(x) for x in seq):
                points += 125
                matches.update(seq_indices)
        
        return points, list(matches)
    
    @staticmethod
    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Optimized: only check up to sqrt(n)
        sqrt_n = int(math.sqrt(n)) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def is_power_of_2(n: int) -> bool:
        # Optimized bit manipulation
        return n > 0 and (n &  (n - 1)) == 0
    
    def use_quantum_power(self):
        if self.quantum_energy > 0 and self.state == GameState.PLAYING:
            self.quantum_energy -= 1
            self.moves_remaining += 5
            self.needs_redraw = True
    
    def game_over(self, reason: str = ""):
        """End the game with a specific reason"""
        self.game_over_reason = reason
        self.state = GameState.GAME_OVER
        self.needs_redraw = True
        print(f"\nGame Over: {reason}")
        print(f"   Final Score: {self.score:,}")
        print(f"   Level: {self.level}\n")
    
    def handle_events(self):
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_click_time < CLICK_COOLDOWN:
                    continue
                
                self.last_click_time = current_time
                self._handle_mouse_click(mouse_pos)
            
            elif event.type == pygame.MOUSEMOTION:
                if self.state == GameState.PLAYING:
                    # Optimized: only check cells if mouse is in grid area
                    grid_left = self.grid_offset_x
                    grid_right = self.grid_offset_x + GRID_SIZE * (CELL_SIZE + GRID_PADDING)
                    grid_top = self.grid_offset_y
                    grid_bottom = self.grid_offset_y + GRID_SIZE * (CELL_SIZE + GRID_PADDING)
                    
                    if grid_left <= mouse_pos[0] <= grid_right and grid_top <= mouse_pos[1] <= grid_bottom:
                        for row in self.cells:
                            for cell in row:
                                old_hover = cell.hover
                                cell_rect = pygame.Rect(cell.x, cell.y, cell.size, cell.size)
                                cell.hover = cell_rect.collidepoint(mouse_pos) and cell.is_empty()
                                if old_hover != cell.hover:
                                    self.needs_redraw = True
            
            elif event.type == pygame.KEYDOWN:
                self._handle_keypress(event.key)
    
    def _handle_mouse_click(self, mouse_pos: Tuple[int, int]):
        if self.state == GameState.MENU:
            if self.buttons['play'].is_clicked(mouse_pos):
                print("Starting game...")
                self.reset_game()
            elif self.buttons['tutorial'].is_clicked(mouse_pos):
                print("Opening tutorial...")
                self.state = GameState.TUTORIAL
                self.tutorial_page = 0
                self.needs_redraw = True
            elif self.buttons['quit'].is_clicked(mouse_pos):
                print("Quitting...")
                self.running = False
        
        elif self.state == GameState.PLAYING:
            if self.buttons['new_game'].is_clicked(mouse_pos):
                print("New game...")
                self.reset_game()
            elif self.buttons['pause'].is_clicked(mouse_pos):
                print("Paused")
                self.state = GameState.PAUSED
                self.needs_redraw = True
            elif self.buttons['help'].is_clicked(mouse_pos):
                print("Help opened")
                self.state = GameState.TUTORIAL
                self.tutorial_page = 0
                self.needs_redraw = True
            else:
                for row in self.cells:
                    for cell in row:
                        cell_rect = pygame.Rect(cell.x, cell.y, cell.size, cell.size)
                        if cell_rect.collidepoint(mouse_pos):
                            self.handle_cell_click(cell.row, cell.col)
                            return
        
        elif self.state == GameState.PAUSED:
            if self.buttons['resume'].is_clicked(mouse_pos):
                print("Resumed")
                self.state = GameState.PLAYING
                self.needs_redraw = True
            elif self.buttons['restart'].is_clicked(mouse_pos):
                print("Restarting...")
                self.reset_game()
            elif self.buttons['menu'].is_clicked(mouse_pos):
                print("Back to menu")
                self.state = GameState.MENU
                self.needs_redraw = True
        
        elif self.state == GameState.GAME_OVER:
            if self.buttons['play_again'].is_clicked(mouse_pos):
                print("Playing again...")
                self.reset_game()
            elif self.buttons['menu_go'].is_clicked(mouse_pos):
                print("Back to menu")
                self.state = GameState.MENU
                self.needs_redraw = True
        
        elif self.state == GameState.TUTORIAL:
            if self.tutorial_page > 0 and self.buttons['tutorial_prev'].is_clicked(mouse_pos):
                self.tutorial_page -= 1
                self.needs_redraw = True
            elif self.tutorial_page < self.max_tutorial_pages - 1 and \
                 self.buttons['tutorial_next'].is_clicked(mouse_pos):
                self.tutorial_page += 1
                self.needs_redraw = True
            elif self.tutorial_page == self.max_tutorial_pages - 1 and \
                 self.buttons['tutorial_close'].is_clicked(mouse_pos):
                print("Starting game from tutorial...")
                self.reset_game()
    
    def _handle_keypress(self, key: int):
        if key == pygame.K_ESCAPE:
            if self.state == GameState.PLAYING:
                self.state = GameState.PAUSED
                self.needs_redraw = True
            elif self.state in [GameState.PAUSED, GameState.TUTORIAL]:
                if self.state == GameState.TUTORIAL:
                    self.state = GameState.MENU
                else:
                    self.state = GameState.PLAYING
                self.needs_redraw = True
            elif self.state == GameState.MENU:
                self.running = False
        
        elif key == pygame.K_n and self.state == GameState.PLAYING:
            self.reset_game()
        
        elif key == pygame.K_p:
            if self.state == GameState.PLAYING:
                self.state = GameState.PAUSED
                self.needs_redraw = True
            elif self.state == GameState.PAUSED:
                self.state = GameState.PLAYING
                self.needs_redraw = True
        
        elif key == pygame.K_q and self.state == GameState.PLAYING:
            if self.quantum_energy > 0:
                print(f"Quantum power used! +5 moves (Energy: {self.quantum_energy-1}/3)")
            self.use_quantum_power()
        
        elif key == pygame.K_h and self.state == GameState.PLAYING:
            self.state = GameState.TUTORIAL
            self.tutorial_page = 0
            self.needs_redraw = True
        
        elif key == pygame.K_f:
            self.show_fps = not self.show_fps
            self.needs_redraw = True
            print(f"FPS Display: {'ON' if self.show_fps else 'OFF'}")
    
    def run(self):
        print(f"\n{'='*60}")
        print(f"  QuantumGrid ULTIMATE v{VERSION}")
        print(f"  LIGHTNING FAST - 120 FPS!")
        print(f"  Perfect UI Alignment - Optimized!")
        print(f"{'='*60}\n")
        print("Controls:")
        print("  Mouse: Click to interact")
        print("  N: New Game | P: Pause | H: Help | Q: Quantum Power")
        print("  F: Toggle FPS | ESC: Pause/Back/Quit\n")
        print("All buttons respond INSTANTLY!\n")
        
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            
            self.handle_events()
            self.update(dt)
            self.draw()
        
        print("\nThanks for playing QuantumGrid ULTIMATE!")
        print(f"   Final High Score: {self.high_score:,}\n")
        self.save_high_score()
        pygame.quit()

def main():
    try:
        game = QuantumGridGame()
        game.run()
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
