
popular_openings = {
    # 1. e4
    "e2e4": {
        "name": "King's Pawn Opening",
        "responses": {
            # 1... e5
            "e7e5": {
                "name": "Open Game",
                "next_moves": {
                    # 2. Nf3
                    "g1f3": {
                        "name": "King's Knight Opening",
                        "responses": {
                            # 2... Nc6
                            "b8c6": {
                                "name": "Ruy Lopez or Italian",
                                "next_moves": {
                                    # 3. Bb5 (Ruy Lopez)
                                    "f1b5": {
                                        "name": "Ruy Lopez",
                                        "responses": {
                                            # 3... a6
                                            "a7a6": {
                                                "name": "Morphy Defense",
                                                "next_moves": {
                                                    # 4. Ba4
                                                    "b5a4": "Closed Ruy Lopez"
                                                }
                                            },
                                            # 3... Nf6
                                            "g8f6": {
                                                "name": "Berlin Defense",
                                                "next_moves": {
                                                    # 4. O-O
                                                    "e1g1": "Berlin Defense Main Line"
                                                }
                                            }
                                        }
                                    },
                                    # 3. Bc4 (Italian Game)
                                    "f1c4": {
                                        "name": "Italian Game",
                                        "responses": {
                                            # 3... Bc5
                                            "f8c5": {
                                                "name": "Giuoco Piano",
                                                "next_moves": {
                                                    # 4. c3
                                                    "c2c3": "Italian Game Main Line"
                                                }
                                            },
                                            # 3... Nf6
                                            "g8f6": {
                                                "name": "Two Knights Defense",
                                                "next_moves": {
                                                    # 4. Ng5
                                                    "g1g5": "Two Knights Defense Main Line"
                                                }
                                            }
                                        }
                                    },
                                    # 3. d4 (Scotch Game)
                                    "d2d4": {
                                        "name": "Scotch Game",
                                        "responses": {
                                            # 3... exd4
                                            "e5d4": {
                                                "name": "Scotch Main Line",
                                                "next_moves": {
                                                    # 4. Nxd4
                                                    "g1d4": "Scotch Game Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            # 2... d6 (Philidor Defense)
                            "d7d6": {
                                "name": "Philidor Defense",
                                "next_moves": {
                                    # 3. d4
                                    "d2d4": "Philidor Main Line"
                                }
                            }
                        }
                    }
                }
            },
            # 1... c5 (Sicilian Defense)
            "c7c5": {
                "name": "Sicilian Defense",
                "next_moves": {
                    # 2. Nf3
                    "g1f3": {
                        "name": "Open Sicilian",
                        "responses": {
                            # 2... d6
                            "d7d6": {
                                "name": "Najdorf or Scheveningen type",
                                "next_moves": {
                                    # 3. d4
                                    "d2d4": {
                                        "name": "Open Sicilian",
                                        "responses": {
                                            # 3... cxd4
                                            "c5d4": {
                                                "name": "Main line",
                                                "next_moves": {
                                                    # 4. Nxd4
                                                    "g1d4": "Open Sicilian Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            # 2... Nc6
                            "b8c6": {
                                "name": "Classical Sicilian",
                                "next_moves": {
                                    # 3. d4
                                    "d2d4": {
                                        "name": "Classical Sicilian",
                                        "responses": {
                                            # 3... cxd4
                                            "c5d4": {
                                                "name": "Classical Main Line",
                                                "next_moves": {
                                                    # 4. Nxd4
                                                    "g1d4": "Classical Sicilian Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            # 1... e6 (French Defense)
            "e7e6": {
                "name": "French Defence",
                "next_moves": {
                    # 2. d4
                    "d2d4": {
                        "name": "Advance or Exchange Variation",
                        "responses": {
                            # 2... d5
                            "d7d5": {
                                "name": "French Main Line",
                                "next_moves": {
                                    # 3. Nc3
                                    "b1c3": {
                                        "name": "Classical",
                                        "responses": {
                                            # 3... Nf6
                                            "g8f6": {
                                                "name": "Classical Main Line",
                                                "next_moves": {
                                                    # 4. Bg5
                                                    "f1g5": "Classical French Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
                            
                        
                    
                
            
        

    # 1. d4
    "d2d4": {
        "name": "Queen's Pawn Opening",
        "responses": {
            # 1... d5
            "d7d5": {
                "name": "Closed Game",
                "next_moves": {
                    # 2. c4 (Queen's Gambit)
                    "c2c4": {
                        "name": "Queen's Gambit",
                        "responses": {
                            # 2... e6 (QGD)
                            "e7e6": {
                                "name": "Queen's Gambit Declined",
                                "next_moves": {
                                    # 3. Nc3
                                    "b1c3": {
                                        "name": "QGD Main Line",
                                        "responses": {
                                            # 3... Nf6
                                            "g8f6": {
                                                "name": "QGD Main Line",
                                                "next_moves": {
                                                    # 4. Bg5
                                                    "f1g5": "QGD Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            # 2... dxc4 (QGA)
                            "d5c4": {
                                "name": "Queen's Gambit Accepted",
                                "next_moves": {
                                    # 3. Nf3
                                    "g1f3": {
                                        "name": "QGA Main Line",
                                        "responses": {
                                            # 3... Nf6
                                            "g8f6": {
                                                "name": "QGA Main Line",
                                                "next_moves": {
                                                    # 4. e3
                                                    "e2e3": "QGA Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    # 2. Nf3 (Colle System or others)
                    "g1f3": "Developing Move"
                }
            },
            # 1... Nf6 (Indian Defence)
            "g8f6": {
                "name": "Indian Defence",
                "next_moves": {
                    # 2. c4
                    "c2c4": {
                        "name": "Main Line",
                        "responses": {
                            # Nimzo-Indian Defense
                            "e7e6": {
                                "name": "Nimzo-Indian Defense",
                                "next_moves": {
                                    # 3. Nc3
                                    "b1c3": {
                                        "name": "Nimzo-Indian Main Line",
                                        "responses": {
                                            # 3... Bb4
                                            "f8b4": {
                                                "name": "Nimzo-Indian Main Line",
                                                "next_moves": {
                                                    # 4. e3
                                                    "e2e3": "Nimzo-Indian Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            },
                            # King's Indian Defense
                            "g7g6": {
                                "name": "King's Indian Defense",
                                "next_moves": {
                                    # 3. Nc3
                                    "b1c3": {
                                        "name": "King's Indian Main Line",
                                        "responses": {
                                            # 3... Bg7
                                            "f8g7": {
                                                "name": "King's Indian Main Line",
                                                "next_moves": {
                                                    # 4. e4
                                                    "e2e4": "King's Indian Main Line"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    },

    # 1. Nf3
    "g1f3": {
        "name": "Réti / Zukertort Opening",
        "responses": {
            "d7d5": {
                "name": "Réti Opening",
                "next_moves": {
                    "c2c4": "Réti Main Line"
                }
            },
            "g8f6": {
                "name": "Réti Opening",
                "next_moves": {
                    "c2c4": "Réti Main Line"
                }
            }
        }
    },

    # 1. c4
    "c2c4": {
        "name": "English Opening",
        "responses": {
            "e7e5": {
                "name": "Reversed Sicilian",
                "next_moves": {
                    "b1c3": "Main Line"
                }
            },
            "c7c5": {
                "name": "Symmetrical Variation",
                "next_moves": {
                    "b1c3": "Main Line"
                }
            }
        }
    }
}
    }
}