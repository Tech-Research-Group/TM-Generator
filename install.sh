pyinstaller main.py --name="TM Generator beta" \
    --onedir \
    --windowed \
    --icon=images/logo_TRG.icns \
    --target-arch=x86_64 \
    --codesign-identity=B2D96E7353EEAD4CCC1D7029A3FA501E5AF91785 \
    --noconfirm --clean \
    --osx-bundle-identifier=com.NicholasRicci.TMShellGenerator \
    --osx-entitlements-file=entitlements.plist
